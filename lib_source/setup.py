from distutils.core import setup, Extension  
  
MOD = 'Elgamal'  
setup(name=MOD, ext_modules=[Extension(MOD, sources=['lib-source.cpp'])])  
