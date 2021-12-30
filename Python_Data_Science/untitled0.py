# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:22:19 2021

@author: DELL
"""
# girilien iki sayının toplama 

sayi1= int(input("1.sayi :"))
sayi2= int(input("2.sayi :"))   
toplam= sayi1+sayi2
print("girilen sayilarin toplami :", toplam)

#%%

sayi1 =float(input("1.sayi :"))
sayi2 =float(input("2.sayi :"))
ortalama =(sayi1 + sayi2)/2;
print(ortalama)

#%% yazılı ortalaması hesaplama geçti kaldı 
not1 = float(input("1.yazılı :"))
not2 = float(input("2.yazılı :"))
ortalama = (not1+not2)/2
print("ortalamanız:",ortalama)
if (ortalama<50):
    print("kaldınız")
else:
    print("tebrikler geçtiniz")

#%%girilen sayinin tek mi çift mi olduğunu bulan program
sayi = int(input("bir sayi girin: "))
if(sayi%2==0):
  print("girdiğiniz sayi çift")
else:
    print("girdiğiniz sayi tek")

#%% girlen sayinin negatif pozitif veya sifir olduğunu bulan program
sayi = int(input("bir sayi girin: "))
if(sayi<0):
    print("sayi negatif")
elif(sayi > 0):
    print("sayi pozitif")
else:
    print("sayi 0")


#%%girilen sayının rakamlarinin carpimi

sayi = 1204

carpim=1
for rakam in str(sayi):
   if int(rakam)!=0 :
    carpim*=int(rakam)
    print("rakamlarin çarpimi: ", carpim)
    
#%%kullanicinin girdigi sayinin rakamlarai taplami

sayi=int(input("bir sayi girin: "))
toplam=0

for rakam in str(sayi):
    toplam+=int(rakam)
    
    print("girilen sayinin  toplami: ", toplam)
    
#%%mutlak deger bulma

sayi=float(input("bir sayi girin:"))
if sayi<0 :
    sayi*=-1
print("sayinin mutlak degeri :",sayi)

#%%
# for i in range(10):
#     print("merhaba dünya")

# sayac=0
# while sayac< 10:
#      sayac =sayac+1
#      print("merhaba dünya")
    
print("merhaba dünya\n"*10)

#%%kullanıcının adını on defa giren program
isim=input("bir isim girin:")
sayac = 0
while sayac<10:
    sayac = sayac+1
    print(isim)
#%%
toplam=0
while True:
    sayi= int(input("sayi girin :"))
    if sayi==0:
        break
    toplam+=sayi
    print("sayilarin toplami: ", toplam)
    
#%% liste elemanları toplama
liste=[10,20,30,40,50]
toplam=0
for i in liste:
    toplam+=i
    #TOPLAM = TOPLAM +SAYİ
    print("sayilaraın topmamı :",toplam)
    #%%sıfır girilenew kadar sayıların ortalaması
sayilar =[]
while True:
    sayi = int(input("sayi giriniz:"))
    if sayi ==0:
        break
    sayilar.append(sayi)
    
toplam=sum(sayilar)
adet =len(sayilar)
print("sayilarin ortalamasi:",toplam/adet)
#%% liste oluştur elaman ekle çıkar
isimler=[]

for i in range(5):
    isimler.append(input("bir isim yazınız: "))
    
for isim in isimler:
    print(isim)
    
#%%ör
isimler = []

for i in range(4):
    isimler.append(input("birisim yaz :"))
    
for isim in isimler:
    print(isim)
#%% liste ortalama
liste =[10,20,30]
toplam =0
adet =len(liste)
for sayi in liste:
    toplam+= sayi
    ortalama =toplam/adet

    print("sayıların ortalaması :",ortalama)
    
#%%
vize= float(input("lütfen vize notunu girin :"))
final = float(input("lütfen final notunu girin: "))


puan=float(vize*0.4 +final*0.6)
ortalama= float(vize +final)/2
if (ortalama>= 50 and puan>50) :
    print("geçtiniz")
else:
    print("kaldınız")
    
#%% map ve zip fonksiyonları

def arttir(x):
    return x*1.2
personel={"ali","veli","can","mustafa","ayhan"}
maas=[1000,2000,3000,4000,5000]
yenimaas=list(map(arttir, maas))
sonuc =list(zip(personel,yenimaas))
print(sonuc)
    
    
    
    
    
