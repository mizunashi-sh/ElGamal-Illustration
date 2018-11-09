#include<string>
#include<iostream>
#include<iosfwd>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<ctime>
#include "Python.h"
#define MAX_L 2005
using namespace std;

//高精度模板
class bign
{
public:
    int len, s[MAX_L];
    bign();
    bign(const char*);
    bign(int);
    bool sign;
    string toStr() const;
    friend istream& operator>>(istream &,bign &);
    friend ostream& operator<<(ostream &,bign &);

    bign operator=(const char*);
    bign operator=(int);
    bign operator=(const string);

    bool operator>(const bign &) const;
    bool operator>=(const bign &) const;
    bool operator<(const bign &) const;
    bool operator<=(const bign &) const;
    bool operator==(const bign &) const;
    bool operator!=(const bign &) const;

    bign operator+(const bign &) const;
    bign operator++();
    bign operator++(int);
    bign operator+=(const bign&);
    bign operator-(const bign &) const;
    bign operator--();
    bign operator--(int);
    bign operator-=(const bign&);
    bign operator*(const bign &)const;
    bign operator*(const int num)const;
    bign operator*=(const bign&);
    bign operator/(const bign&)const;
    bign operator/=(const bign&);

    bign operator%(const bign&)const;
    bign factorial()const;
    bign Sqrt()const;
    bign pow(const bign&)const;

    void clean();
};
#define max(a,b) a>b ? a : b
#define min(a,b) a<b ? a : b

bign::bign()
{
    memset(s, 0, sizeof(s));
    len = 1;
    sign = 1;
}

bign::bign(const char *num)
{
    *this = num;
}

bign::bign(int num)
{
    *this = num;
}

string bign::toStr() const
{
    string res;
    res = "";
    for (int i = 0; i < len; i++)
        res = (char)(s[i] + '0') + res;
    if (res == "")
        res = "0";
    if (!sign&&res != "0")
        res = "-" + res;
    return res;
}

istream &operator>>(istream &in, bign &num)
{
    string str;
    in>>str;
    num=str;
    return in;
}

ostream &operator<<(ostream &out, bign &num)
{
    out<<num.toStr();
    return out;
}

bign bign::operator=(const char *num)
{
    memset(s, 0, sizeof(s));
    char a[MAX_L] = "";
    if (num[0] != '-')
        strcpy(a, num);
    else
        for (int i = 1; i < strlen(num); i++)
            a[i - 1] = num[i];
    sign = !(num[0] == '-');
    len = strlen(a);
    for (int i = 0; i < strlen(a); i++)
        s[i] = a[len - i - 1] - 48;
    return *this;
}

bign bign::operator=(int num)
{
    char temp[MAX_L];
    sprintf(temp,"%d", num);
    *this = temp;
    return *this;
}

bign bign::operator=(const string num)
{
    const char *tmp;
    tmp = num.c_str();
    *this = tmp;
    return *this;
}

bool bign::operator<(const bign &num) const
{
    if (sign^num.sign)
        return num.sign;
    if (len != num.len)
        return len < num.len;
    for (int i = len - 1; i >= 0; i--)
        if (s[i] != num.s[i])
            return sign ? (s[i] < num.s[i]) : (!(s[i] < num.s[i]));
    return !sign;
}

bool bign::operator>(const bign&num)const
{
    return num < *this;
}

bool bign::operator<=(const bign&num)const
{
    return !(*this>num);
}

bool bign::operator>=(const bign&num)const
{
    return !(*this<num);
}

bool bign::operator!=(const bign&num)const
{
    return *this > num || *this < num;
}

bool bign::operator==(const bign&num)const
{
    return !(num != *this);
}

bign bign::operator+(const bign &num) const
{
    if (sign^num.sign)
    {
        bign tmp = sign ? num : *this;
        tmp.sign = 1;
        return sign ? *this - tmp : num - tmp;
    }
    bign result;
    result.len = 0;
    int temp = 0;
    for (int i = 0; temp || i < (max(len, num.len)); i++)
    {
        int t = s[i] + num.s[i] + temp;
        result.s[result.len++] = t % 10;
        temp = t / 10;
    }
    result.sign = sign;
    return result;
}

bign bign::operator++()
{
    *this = *this + 1;
    return *this;
}

bign bign::operator++(int)
{
    bign old = *this;
    ++(*this);
    return old;
}

bign bign::operator+=(const bign &num)
{
    *this = *this + num;
    return *this;
}

bign bign::operator-(const bign &num) const
{
    bign b=num,a=*this;
    if (!num.sign && !sign)
    {
        b.sign=1;
        a.sign=1;
        return b-a;
    }
    if (!b.sign)
    {
        b.sign=1;
        return a+b;
    }
    if (!a.sign)
    {
        a.sign=1;
        b=bign(0)-(a+b);
        return b;
    }
    if (a<b)
    {
        bign c=(b-a);
        c.sign=false;
        return c;
    }
    bign result;
    result.len = 0;
    for (int i = 0, g = 0; i < a.len; i++)
    {
        int x = a.s[i] - g;
        if (i < b.len) x -= b.s[i];
        if (x >= 0) g = 0;
        else
        {
            g = 1;
            x += 10;
        }
        result.s[result.len++] = x;
    }
    result.clean();
    return result;
}

bign bign::operator * (const bign &num)const
{
    bign result;
    result.len = len + num.len;

    for (int i = 0; i < len; i++)
        for (int j = 0; j < num.len; j++)
            result.s[i + j] += s[i] * num.s[j];

    for (int i = 0; i < result.len; i++)
    {
        result.s[i + 1] += result.s[i] / 10;
        result.s[i] %= 10;
    }
    result.clean();
    result.sign = !(sign^num.sign);
    return result;
}

bign bign::operator*(const int num)const
{
    bign x = num;
    bign z = *this;
    return x*z;
}
bign bign::operator*=(const bign&num)
{
    *this = *this * num;
    return *this;
}

bign bign::operator /(const bign&num)const
{
    bign ans;
    ans.len = len - num.len + 1;
    if (ans.len < 0)
    {
        ans.len = 1;
        return ans;
    }

    bign divisor = *this, divid = num;
    divisor.sign = divid.sign = 1;
    int k = ans.len - 1;
    int j = len - 1;
    while (k >= 0)
    {
        while (divisor.s[j] == 0) j--;
        if (k > j) k = j;
        char z[MAX_L];
        memset(z, 0, sizeof(z));
        for (int i = j; i >= k; i--)
            z[j - i] = divisor.s[i] + '0';
        bign dividend = z;
        if (dividend < divid) { k--; continue; }
        int key = 0;
        while (divid*key <= dividend) key++;
        key--;
        ans.s[k] = key;
        bign temp = divid*key;
        for (int i = 0; i < k; i++)
            temp = temp * 10;
        divisor = divisor - temp;
        k--;
    }
    ans.clean();
    ans.sign = !(sign^num.sign);
    return ans;
}

bign bign::operator/=(const bign&num)
{
    *this = *this / num;
    return *this;
}

bign bign::operator%(const bign& num)const
{
    bign a = *this, b = num;
    a.sign = b.sign = 1;
    bign result, temp = a / b*b;
    result = a - temp;
    result.sign = sign;
    return result;
}

bign bign::pow(const bign& num)const
{
    bign result = 1;
    for (bign i = 0; i < num; i++)
        result = result*(*this);
    return result;
}

bign bign::factorial()const
{
    bign result = 1;
    for (bign i = 1; i <= *this; i++)
        result *= i;
    return result;
}

void bign::clean()
{
    if (len == 0) len++;
    while (len > 1 && s[len - 1] == '\0')
        len--;
}

bign bign::Sqrt()const
{
    if(*this<0)return -1;
    if(*this<=1)return *this;
    bign l=0,r=*this,mid;
    while(r-l>1)
    {
        mid=(l+r)/2;
        if(mid*mid>*this)
            r=mid;
        else
            l=mid;
    }
    return l;
}

//快速幂取模
bign fastmod(bign a,bign b,bign mod)
{
    bign sum = 1;
	a = a % mod;

	while (b > 0) {
		if (b % 2 == 1)
			sum = (sum * a) % mod;

		b = b/2;
		a = (a * a) % mod;
	}
	return sum;
}

//求逆元算法
bign inverse(bign a,bign p)
{
    const bign temp=2;

    return fastmod(a,p-temp,p);
}

//求原根算法
//q为任意大素数,同时p=2*q+1也是素数
//返回p的原根
char* primitive(char* q_str)
{
    bign q=q_str;
    bign p=q*2+1;
    bign g;
    bign rand_temp;
    char result_array[MAX_L];
    char *result=result_array;

    srand(time(NULL));
    do{
        rand_temp=rand();
        g=rand_temp%p;
        if(g<2)
            g+=2;
    }while(fastmod(g,2,p)==1||fastmod(q,2,p)==1);

    sprintf(result_array,"%s",g.toStr().c_str());
    return result;
}

//Miller-Rabin素性测试
bool miller_rabin(bign num)
{
    bign d=num-1;
    bign rand_temp,i;

    srand(time(NULL));
    rand_temp=rand();
    i=rand_temp%num;
    if(i<2)
        i=i+2;
    while(d!=1)
    {
        if(fastmod(i,d,num)==1)
        {
            if(d%2!=0)
                return true;
            d=d/2;
            if(fastmod(i,d,num)==num-1)
                return true;
        }
        else
            return false;
    }
    return true;
}

//生成大素数q,使得p=2*q+1也是素数
char *generate_prime_q(char *num_str)
{
    const bign a=2,b=1;
    bign num=num_str;
    bign p=a*num+b;
    int i=0;
    bool flag=true,temp=true;
    char result_array[MAX_L];
    char *result=result_array;

    while(flag)
    {
        while(!(miller_rabin(num)&&miller_rabin(p)))
        {
            num=num+1;
            p=a*num+b;
        }
        if(miller_rabin(num)&&miller_rabin(p))
        {
            while(i<3&&temp)
            {
                temp=miller_rabin(num)&&miller_rabin(p);
                i+=1;
            }
            if(i==3)
                flag=false;
            else if(!temp)
            {
                num=num+1;
                p=a*num+b;
            }
        }
    }

    sprintf(result_array,"%s",num.toStr().c_str());
    return result;
}

//生成大素数p=2*q+1,q也是素数
char *generate_prime_p(char *num_str)
{
    const bign a=2,b=1;
    bign num=num_str;
    char result_array[MAX_L];
    char *result=result_array;

    num=num*a+b;
    sprintf(result_array,"%s",num.toStr().c_str());
    return result;
}

//生成随机数1<k<p-1
char *generate_random(char *p_str)
{
    bign k,p=p_str;
    bign rand_temp;
    char result_array[MAX_L];
    char *result=result_array;

    srand(time(NULL));
    rand_temp=rand();
    k=rand_temp%(p-1);
    if(k<2)
        k=k+2;
    sprintf(result_array,"%s",k.toStr().c_str());
    return result;
}

//生成公钥
//a为原根，priv为私钥，p为大素数
char *generate_public(char *a_str,char *priv_str,char *p_str)
{
    bign a=a_str,priv=priv_str,p=p_str;
    bign pub;
    char result_array[MAX_L];
    char *result=result_array;

    pub=fastmod(a,priv,p);
    sprintf(result_array,"%s",pub.toStr().c_str());
    return result;
}

//生成密文C1,a为原根,k为随机数,p为大素数
char * generate_cipher_1(char *a_str, char* k_str,char *p_str)
{
    bign a=a_str,k=k_str,p=p_str;
    bign c1;
    char result_array[MAX_L];
    char *result=result_array;

    c1=fastmod(a,k,p);
    sprintf(result_array,"%s",c1.toStr().c_str());
    return result;
}

//生成密文C2,pub为公钥,k为随机数,p为大素数,plain为原文
char * generate_cipher_2(char *pub_str,char *k_str,char *p_str,char *plain)
{
    bign pub=pub_str,k=k_str,p=p_str;
    bign temp_key;
    bign c2,plain_int;
    char result_array[MAX_L];
    char *result=result_array;

    temp_key=fastmod(pub,k,p);
    if(plain[0]<2)
        plain_int=(int)plain[0]+128;
    else
        plain_int=(int)plain[0];
    c2=(plain_int*temp_key)%p;
    sprintf(result_array,"%s",c2.toStr().c_str());
    return result;
}

//解密函数
char decrypt(char *c1_str,char *c2_str,char *priv_str,char *p_str)
{
    bign c1,c2,priv,p,K,k,M;//K为密钥，k为K对p的逆元
    c1=c1_str;
    c2=c2_str;
    priv=priv_str;
    p=p_str;
    K=fastmod(c1,priv,p);
    k=inverse(K,p);
    M=fastmod(c2*k,1,p);
    string M_string=M.toStr();
    const char*M_str=M_string.c_str();
    printf("%s\n",M_str);
    int M_int=atoi(M_str);
    if(M_int==128)
        M_int=0;
    else if(M_int==129)
        M_int=1;
    return (char)M_int;
}

//以下是为Python封装的函数接口
//生成大素数q,并使得p=2q+1也是素数
static PyObject * Elgamal_generate_q(PyObject * self,PyObject * args){
    char *num_str;
    PyObject *retval;

    if(!PyArg_ParseTuple(args, "s", &num_str)){
        return NULL;
    }
    retval=(PyObject*)Py_BuildValue("s", generate_prime_q(num_str));
    return retval;
}

//生成随机数1<k<p-1
static PyObject * Elgamal_generate_random(PyObject * self,PyObject * args){
    char *p_str;
    PyObject *retval;

    if(!PyArg_ParseTuple(args, "s", &p_str)){
        return NULL;
    }
    retval=(PyObject*)Py_BuildValue("s", generate_random(p_str));
    return retval;
}

//由q生成大素数p
static PyObject * Elgamal_generate_p(PyObject * self,PyObject * args){
    char *q_str;
    PyObject *retval;

    if(!PyArg_ParseTuple(args, "s", &q_str)){
        return NULL;
    }
    retval=(PyObject*)Py_BuildValue("s", generate_prime_p(q_str));
    return retval;
}

//求p的原根,参数为q,使得p=2*q+1
static PyObject * Elgamal_primitive(PyObject * self,PyObject * args){
    char *q_str;
    PyObject *retval;

    if(!PyArg_ParseTuple(args, "s", &q_str)){
        return NULL;
    }
    retval=(PyObject*)Py_BuildValue("s", primitive(q_str));
    return retval;
}

//获取公钥
static PyObject * Elgamal_get_public(PyObject * self,PyObject * args){
    char *a_str;
    char *priv_str;
    char *p_str;
    PyObject *retval;

    if(!PyArg_ParseTuple(args, "sss", &a_str,&priv_str,&p_str)){
        return NULL;
    }
    retval=(PyObject*)Py_BuildValue("s", generate_public(a_str,priv_str,p_str));
    return retval;
}

//获取密文C1
static PyObject * Elgamal_get_cipher_1(PyObject * self,PyObject * args){
    char *a_str;
    char *k_str;
    char *p_str;
    PyObject *retval;

    if(!PyArg_ParseTuple(args, "sss", &a_str,&k_str,&p_str)){
        return NULL;
    }
    retval=(PyObject*)Py_BuildValue("s", generate_cipher_1(a_str,k_str,p_str));
    return retval;
}

//获取密文C2
static PyObject * Elgamal_get_cipher_2(PyObject * self,PyObject * args){
    char *pub_str;
    char *k_str;
    char *p_str;
    char *plain;
    PyObject *retval;

    if(!PyArg_ParseTuple(args, "ssss", &pub_str,&k_str,&p_str,&plain)){
        return NULL;
    }
    retval=(PyObject*)Py_BuildValue("s", generate_cipher_2(pub_str,k_str,p_str,plain));
    return retval;
}

static PyObject * Elgamal_decrypt(PyObject * self,PyObject * args){
    char *c1_str;
    char *c2_str;
    char *priv_str;
    char *p_str;
    PyObject *retval;

    if(!PyArg_ParseTuple(args, "ssss", &c1_str,&c2_str,&priv_str,&p_str)){
        return NULL;
    }
    retval=(PyObject*)Py_BuildValue("c", decrypt(c1_str,c2_str,priv_str,p_str));
    return retval;
}

static PyMethodDef ElgamalMethods[] =
{
    { "generate_q", Elgamal_generate_q, METH_VARARGS },
    { "generate_p", Elgamal_generate_p, METH_VARARGS },
    { "generate_random", Elgamal_generate_random, METH_VARARGS },
    { "primitive", Elgamal_primitive, METH_VARARGS },
    { "get_public", Elgamal_get_public, METH_VARARGS },
    { "get_cipher_1", Elgamal_get_cipher_1, METH_VARARGS },
    { "get_cipher_2", Elgamal_get_cipher_2, METH_VARARGS },
    { "decrypt", Elgamal_decrypt, METH_VARARGS },
    { NULL, NULL },
};

static struct PyModuleDef Elgamal =
{
    PyModuleDef_HEAD_INIT,
    "Elgamal",
    "",
    -1,
    ElgamalMethods
};

PyMODINIT_FUNC PyInit_Elgamal(void)
{
    return PyModule_Create(&Elgamal);
}

