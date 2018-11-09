import wx
import Elgamal


class Generate(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(700, 600), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"The big prime p:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        self.m_staticText2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOTEXT))

        bSizer3.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_READONLY)
        bSizer3.Add(self.m_textCtrl3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"The primitive root a:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        bSizer3.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_READONLY)
        bSizer3.Add(self.m_textCtrl7, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"Public Key:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        bSizer3.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_textCtrl8 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_READONLY)
        bSizer3.Add(self.m_textCtrl8, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Enter Private Key(Make it < p):", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        bSizer3.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_textCtrl9 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize)
        bSizer3.Add(self.m_textCtrl9, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"Enter a big number:", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText17.Wrap(-1)

        bSizer3.Add(self.m_staticText17, 0, wx.ALL, 5)

        self.m_textCtrl17 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_textCtrl17, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"Generate p,a", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Generate keys", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_button4.Disable()
        self.SetSizer(bSizer3)
        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.generate_prime, self.m_button2)
        self.Bind(wx.EVT_BUTTON, self.generate_keys, self.m_button4)
        self.Bind(wx.EVT_BUTTON, self.clear_text, self.m_button5)

    def generate_prime(self, event):
        self.m_button4.Disable()
        num = self.m_textCtrl17.GetValue()
        if num == "":
            dlg = wx.MessageDialog(None, "Please Enter a number!", "Error")
            dlg.ShowModal()
            dlg.Destroy()
            return
        self.m_button2.Disable()
        self.m_button2.SetLabel(u"Generating...")
        q = Elgamal.generate_q(num)
        p = Elgamal.generate_p(q)
        a = Elgamal.primitive(q)
        self.m_textCtrl3.write(p)
        self.m_textCtrl7.write(a)
        self.m_button2.Enable()
        self.m_button2.SetLabel(u"Generate p,a")

        self.m_button4.Enable()

    def generate_keys(self, event):
        self.m_button4.Disable()
        self.m_button4.SetLabel("Generating...")
        p = self.m_textCtrl3.GetValue()
        a = self.m_textCtrl7.GetValue()
        priv = self.m_textCtrl9.GetValue()
        if priv == "":
            dlg = wx.MessageDialog(None, "Please Enter a number!", "Error")
            dlg.ShowModal()
            dlg.Destroy()
            self.m_button4.Enable()
            self.m_button4.SetLabel("Generate Keys")
            return
        pub = Elgamal.get_public(a, priv, p)
        self.m_textCtrl8.write(pub)
        self.m_button4.Enable()
        self.m_button4.SetLabel("Generate Keys")

    def clear_text(self, event):
        self.m_textCtrl3.Clear()
        self.m_textCtrl7.Clear()
        self.m_textCtrl8.Clear()


class Encrypt(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(700, 600), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Enter the plain text:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        bSizer4.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl5, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"Enter the primitive root a:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        bSizer4.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl6, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"Enter the big prime p:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        bSizer4.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl7, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"Enter the public key:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        bSizer4.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.m_textCtrl9 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl9, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"Cipher Text 1:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)

        bSizer4.Add(self.m_staticText10, 0, wx.ALL, 5)

        self.m_textCtrl10 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.TE_READONLY)
        bSizer4.Add(self.m_textCtrl10, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Cipher Text 2:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)

        bSizer4.Add(self.m_staticText11, 0, wx.ALL, 5)

        self.m_textCtrl11 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_MULTILINE | wx.TE_READONLY)
        bSizer4.Add(self.m_textCtrl11, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"Encrypt", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button6, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.generate_cipher, self.m_button2)
        self.Bind(wx.EVT_BUTTON, self.clear_text, self.m_button6)

    def generate_cipher(self, event):
        plain = self.m_textCtrl5.GetValue()
        a = self.m_textCtrl6.GetValue()
        p = self.m_textCtrl7.GetValue()
        k = Elgamal.generate_random(p)
        pub = self.m_textCtrl9.GetValue()
        if a == "" or plain == "" or p == "" or pub == "":
            dlg = wx.MessageDialog(None, "Please Enter a value!", "Error")
            dlg.ShowModal()
            dlg.Destroy()
            return
        self.m_button2.Disable()
        self.m_button2.SetLabel(u"Encrypting...")
        cipher_1 = Elgamal.get_cipher_1(a, k, p)
        self.m_textCtrl10.write(cipher_1)
        for plain_letter in plain:
            cipher_2 = Elgamal.get_cipher_2(pub, k, p, plain_letter)
            self.m_textCtrl11.write(cipher_2)
            self.m_textCtrl11.write(' ')
        self.m_button2.Enable()
        self.m_button2.SetLabel(u"Encrypt")

    def clear_text(self, event):
        self.m_textCtrl10.Clear()
        self.m_textCtrl11.Clear()


class Decrypt(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(700, 600), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"Enter the cipher text 1:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)

        bSizer3.Add(self.m_staticText12, 0, wx.ALL, 5)

        self.m_textCtrl12 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_textCtrl12, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText14 = wx.StaticText(self, wx.ID_ANY, u"Enter the cipher text2:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)

        bSizer3.Add(self.m_staticText14, 0, wx.ALL, 5)

        self.m_textCtrl13 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_textCtrl13, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText15 = wx.StaticText(self, wx.ID_ANY, u"Enter the big prime p:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)

        bSizer3.Add(self.m_staticText15, 0, wx.ALL, 5)

        self.m_textCtrl14 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_textCtrl14, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText16 = wx.StaticText(self, wx.ID_ANY, u"Enter the private key:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)

        bSizer3.Add(self.m_staticText16, 0, wx.ALL, 5)

        self.m_textCtrl15 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_textCtrl15, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"The plain text:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)

        bSizer3.Add(self.m_staticText17, 0, wx.ALL, 5)

        self.m_textCtrl16 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_READONLY)
        bSizer3.Add(self.m_textCtrl16, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"Decrypt", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button3, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_button7 = wx.Button(self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button7, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.decrypt, self.m_button3)
        self.Bind(wx.EVT_BUTTON, self.clear_text, self.m_button7)

    def decrypt(self, event):
        c1 = self.m_textCtrl12.GetValue()
        c2 = self.m_textCtrl13.GetValue()
        c2_list = c2.split()
        p = self.m_textCtrl14.GetValue()
        priv = self.m_textCtrl15.GetValue()
        if c1 == "" or c2 == "" or p == "" or priv == "":
            dlg = wx.MessageDialog(None, "Please Enter a value!", "Error")
            dlg.ShowModal()
            dlg.Destroy()
            return
        self.m_button3.Disable()
        self.m_button3.SetLabel("Decrypting...")
        for cipher in c2_list:
            self.m_textCtrl16.write(Elgamal.decrypt(c1, cipher, priv, p))
        self.m_button3.Enable()
        self.m_button3.SetLabel("Decrypt")

    def clear_text(self, event):
        self.m_textCtrl16.Clear()


class Manual(wx.Panel):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(700, 600), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"Step 1:生成密钥", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)

        bSizer4.Add(self.m_staticText17, 0, wx.ALL, 5)

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, u"1.在“Generate Keys\"标签的最后一个输入框内随意输入一个大整数",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)

        bSizer4.Add(self.m_staticText18, 0, wx.ALL, 5)

        self.m_staticText19 = wx.StaticText(self, wx.ID_ANY, u"2.点击”Generate p,a\"生成密钥第一部分", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)

        bSizer4.Add(self.m_staticText19, 0, wx.ALL, 5)

        self.m_staticText20 = wx.StaticText(self, wx.ID_ANY, u"3.密钥第一部分生成成功后，在倒数第二个输入框填入私钥，注意私钥必须为正整数且要比p小",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText20.Wrap(-1)

        bSizer4.Add(self.m_staticText20, 0, wx.ALL, 5)

        self.m_staticText21 = wx.StaticText(self, wx.ID_ANY, u"4.点击Generate keys生成公钥", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)

        bSizer4.Add(self.m_staticText21, 0, wx.ALL, 5)

        self.m_staticText22 = wx.StaticText(self, wx.ID_ANY, u"注意：生成密钥第一部分于公钥时，不要对计算机进行任何操作，并且关闭尽可能多的后台进程",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)

        bSizer4.Add(self.m_staticText22, 0, wx.ALL, 5)

        self.m_staticText23 = wx.StaticText(self, wx.ID_ANY, u"      这样方可确保生成成功", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText23.Wrap(-1)

        bSizer4.Add(self.m_staticText23, 0, wx.ALL, 5)

        self.m_staticText24 = wx.StaticText(self, wx.ID_ANY, u"      请保管好私钥", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText24.Wrap(-1)

        bSizer4.Add(self.m_staticText24, 0, wx.ALL, 5)

        self.m_staticText25 = wx.StaticText(self, wx.ID_ANY, u"Step2:加密", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText25.Wrap(-1)

        bSizer4.Add(self.m_staticText25, 0, wx.ALL, 5)

        self.m_staticText26 = wx.StaticText(self, wx.ID_ANY, u"1.在第一个输入框内填入明文", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText26.Wrap(-1)

        bSizer4.Add(self.m_staticText26, 0, wx.ALL, 5)

        self.m_staticText27 = wx.StaticText(self, wx.ID_ANY, u"2.在剩余输入框内填入之前生成的密钥", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText27.Wrap(-1)

        bSizer4.Add(self.m_staticText27, 0, wx.ALL, 5)

        self.m_staticText28 = wx.StaticText(self, wx.ID_ANY, u"3.点击Encrypt生成密文", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText28.Wrap(-1)

        bSizer4.Add(self.m_staticText28, 0, wx.ALL, 5)

        self.m_staticText29 = wx.StaticText(self, wx.ID_ANY, u"Step3:解密", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText29.Wrap(-1)

        bSizer4.Add(self.m_staticText29, 0, wx.ALL, 5)

        self.m_staticText30 = wx.StaticText(self, wx.ID_ANY, u"1.在输入框内填入之前生成的各种信息", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText30.Wrap(-1)

        bSizer4.Add(self.m_staticText30, 0, wx.ALL, 5)

        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, u"2.点击Decrypt获取明文", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)

        bSizer4.Add(self.m_staticText31, 0, wx.ALL, 5)

        self.m_staticText32 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText32.Wrap(-1)

        bSizer4.Add(self.m_staticText32, 0, wx.ALL, 5)

        self.m_staticText33 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText33.Wrap(-1)

        bSizer4.Add(self.m_staticText33, 0, wx.ALL, 5)

        self.m_staticText34 = wx.StaticText(self, wx.ID_ANY, u"注意：在生成密钥、加密于解密之后，如需进行相同操作，请先按Clear键", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText34.Wrap(-1)

        bSizer4.Add(self.m_staticText34, 0, wx.ALL, 5)

        self.SetSizer(bSizer4)
        self.Layout()


app = wx.App(False)
frame = wx.Frame(None, title="ElGamal Encryptor", size=wx.Size(700, 600))
nb = wx.Notebook(frame)
nb.AddPage(Manual(nb), "Manual")
nb.AddPage(Generate(nb), "Generate Key")
nb.AddPage(Encrypt(nb), "Encrypt")
nb.AddPage(Decrypt(nb), "Decrypt")
frame.Show()
app.MainLoop()

