# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:55:32 2021

@author: DELL
"""

#%%
#list

liste = [1,2,3,4,5,6,]
type(liste)

liste_str = ["ptesi","sali","cars"]
type(liste_str)

value = liste[1]
print(value)

last_value = liste[-1]

liste_devide = liste[0:3]

liste.append(7)
liste.remove(7)
liste.reverse()


liste2 = [1,5,12,6,7,4,9,8]
liste2.sort()
string_int_list = [1,2,3,"aa","bb "]

#%%
#dictionary
dictionary = {"ali":32,"veli":45,"aysen":13}

def deneme():
    dictionary = {"ali":32,"veli":45,"aysen":13}
    return dictionary

dic = deneme()

#%%
#conditionals
#if else statement


var1 = 10
var2 = 20

if (var1>var2):
    print("var1 büyüktür var2")
elif(var1>var2):
    print("var1 ve var2 eşittir")
else:
    print("var1 küçüktür var2")
   

liste = [1,2,3,4,5]
value = 3

if value in liste:
    print("evet {} değeri listenin içinde".format(value))
else:
    print("hayir")    

keys = dictionary.keys()

if "a" in keys:
    print("evet")
else:
    print("hayır")
    
#%%
#1640.yıl = 17.yüzyıl
# 109.yıl =2.yüzyıl

#metod yazın,
# input integer yıllar
#output yüzyıl
# input = year >> 1 <= year <=2005

def year2Century(year):
    """
    year to century

    Parameters
    ----------
    year : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    
    str_year = str(year)  
    
    if(len(str_year)<3):
        return 1
    elif(len(str_year)==3):
        if(str_year[1:3]=="00"): #100,200,300,400.....900
           return int (str_year[0])
        else:    #190 , 250, 370 ....
           return int (str-year[0])+1
    else:    #1700,1800,1900
        if (str_year[2:4]=="00"):
            return int(str_year[:2])
        else: #1705,1810,1930
            return int(str_year[:2])+1
            
        
#%%loop
#for loop

for each in range(1,11):
    print(each)
for each in "ankara ist":
    print(each)
    
for each in "ankara ist".split():
    print(each)
    
listes = [1,2,5,6,8,9,10,67,15]

summation = sum(listes)

count=0
for each in listes:
    count = count+each
    print(count)
    
#while loop

i = 0
while (i < 4):
    print(i)
    i = i+1

sinir = len(listes)
each = 0
count = 0
while(each<sinir):
    count=count +listes[each]
    each=each+1
    
    
#%%
#liste verilecek 
#bu listenin içindeki en küçük sayıyı bul

liste1 = [1,52,23,12,15,16,26,158,-124,3]

mini = 1000000
for each in liste1:
    if (each<min):
        min = each
    else:
        continue
    

 


