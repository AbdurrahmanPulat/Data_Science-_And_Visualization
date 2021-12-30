# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 15:41:00 2021

@author: DELL
"""

class Calisan:
    
    zam_orani =1.8
    counter = 0
    def  __init__(self,isim,soyisim,maas): #constructor
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim +"@asd.com"
        
        Calisan.counter =Calisan.counter + 1
    
    def giveNameSurname(self):
        return self.isim+ " "+self.soyisim
    
    def zam_yap(self):
        self.maas = self.maas+ self.maas*self.zam_orani
        

# isci1 = Calisan("ali","veli",100)
# print(isci1.maas)
# print(isci1.giveNameSurname())

#class veiable
        
calisan1 =Calisan("ali","veli",100)
print(" alinin ilk maası:",calisan1.maas)
calisan1.zam_yap()
print("alinin yeni maas:",calisan1.maas)

calisan2 = Calisan("ayse", "hatice",200)
calisan3 = Calisan("abdurrahman","polat",1000)
print(" abdurrahmanın ilk maası:",calisan3.maas)
calisan3.zam_yap()
print("abdurrahmanın yeni maası:",calisan3.maas)
calisan4 = Calisan("hilal", "caice",500)
calisan5 = Calisan("mustafa", "can",400)
calisan6  = Calisan("yelda", "hatice",300)

liste = [calisan1,calisan2,calisan3,calisan4,calisan5,calisan6]

maxi_maas = -1
index = -1

for each in liste:
    if(each.maas>maxi_maas):
        maxi_maas = each.maas
        index=each
        
print(maxi_maas)
print(index.giveNameSurname())