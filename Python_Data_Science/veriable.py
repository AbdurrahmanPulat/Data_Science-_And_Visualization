# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 08:37:50 2021

@author: DELL
"""
#%%
#veriable(degisken)
#veriable
#function
#object

var1= 10 
var2 = 15

gun ="pazartesi"

var3= 10.0



#%%

#string

s = "bugün günlerden pazartesi"


veriable_type = type(s)

print(s)

var1 = "ankara"
var2= "istanbul"
var3= var1 +var2
print(var3)

uzunluk = len(var3)
#%%
integer_deneme = -50
float_deneme = -30.5

#%% built in function

str1="deneme"
float1 = 10.6
str2 = "1005"

#%%# user defined functions

var1 = 20
var2 = 50

output = (((var1+var2)*50)/100.0)*var1/var2

def benim_ilk_func(var1,var2):
    """
    bu benim ilk projem
    
    parametre:
    
    return:
    """
            
    output = (((var1+var2)*50)/100.0)*var1/var2
    
    return output
sonuc = benim_ilk_func(var1,var2)

def deneme1():

    print("bu benim ikinci denemem")
#%% default and flexible functions

# default çemberin çevresinin uzunluğu = 2*pi*r

def cember_cevresi_hesapla(r,pi =3.14):
    """
  cember  cevresi hesapla
  input(parametre): r,pi
  output = cemberin cevresi
  """
    output = 2*pi*r
    return output
#flexible

# def hesapla (boy,kilo,*args):
#     print(len(args))
#     output =boy+kilo
#     return output

def hesapla (boy,kilo,*args):
    print(args)
    output = (boy+kilo)*args[0]
    return output

# def hesapla (boy,kilo,yas):
#     output =(boy+kilo)*yas
#     return output


#%%QUIZ
  
# İNT VERİABLE yas
# string name isim
# function olacak
# fonksiyon print(type(),len,float())
#*args soyisim
# default parametre ayakkabı numarasi

yas= 10
name ="ali"
soyisim = "veli"

def function_quiz(yas,name,*args,ayakkabi_numarasi = 35):
    print("cocugun ismi: ",name,"yasi: ",yas," ayak numarasi: ",ayakkabi_numarasi)
    print(type(name))
    print(float(yas))
    
    output = args[0]*yas
    
    return output

sonuc = function_quiz(yas,name,soyisim)

print("args[0]*yas: ",sonuc)
#%%
#lambda function
    
def hesapla(x):
    output = x*x
    return output
sonuc = hesapla(3)

sonuc2 = lambda x:x*x

print(sonuc2(3))
    

  



 
         

