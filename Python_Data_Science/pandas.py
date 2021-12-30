# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 08:14:06 2021

@author: DELL
"""

# 1) pandas hızlı ve etkili bir dataframes
# 2) csv ve text dosyalarını açıp sonuçlarımıza bu dosya tiplerine bir şekilde kaydedebilir
# 3) Pandas bizim işimizi kolaylaştırıyor for missing data
# 4)reshape yapıp datayı daha etkili bir şekilde kulllanabiliriz
# 5)slicing indexing kolay
# 6) time series data analizinde çok yardımcı
# 7) ayrıca herşeyden önemlisi hız ,pandas hız açısından optimize edilmiş bir kütüphane

import pandas as pd

dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]}


dataFrame1 = pd.DataFrame(dictionary)
head = dataFrame1.head() #ilk beş datayı gösterir
tail = dataFrame1.tail() # son 5 datayı gösterir parantezin içine kaç rakamı girerseniz o kadar data gösterir

#%%
#pandas basic metodları

print(dataFrame1.columns)
print(dataFrame1.info())

print(dataFrame1.dtypes)
print(dataFrame1.describe()) #numeric feature = colums (age ,maaas)
#%%

print(dataFrame1["AGE"])

print(dataFrame1.AGE)

dataFrame1["yeni_feature"] = [-1,-2,-3,-4,-5,-6]

print(dataFrame1.loc[:,"AGE"])

print(dataFrame1.loc[:3, "AGE"])
print(dataFrame1.loc[:3, "NAME":"AGE"])
print(dataFrame1.loc[:3, ["AGE","NAME"]])

print(dataFrame1.loc[::-1,:]) #tersten yazdır
print(dataFrame1.loc[:,:"MAAS"])
print(dataFrame1.loc[:,"MAAS"])
print(dataFrame1.iloc[:,2])

#%%FİLTERİNG

filtre1 = dataFrame1.MAAS > 200

filtrelenmis_data =dataFrame1[filtre1]

filtre2 = dataFrame1.AGE < 20

dataFrame1[filtre1 & filtre2]

dataFrame1[dataFrame1.AGE > 60]

#%%list comprehension
import numpy as np

ortalama_maas = dataFrame1.MAAS.mean()
 
#ortalama_maas_np =np.mean(dataFrame1.MAAS)
 
dataFrame1["maas_seviyesi"] = ["dusuk" if ortalama_maas > each else "yuksek" for each in dataFrame1.MAAS]

# for each in dataFrame1.MAAS:
#     if(ortalama_maas > each):
#         print("yüksek")
        
#     else:
#         print("dusuk")


dataFrame1.columns = [each.lower() for each in dataFrame1.columns]

#%%drop and concatenating

dataFrame1.drop (["yeni_feature"],axis=1,inplace = True)
                     
data1 = dataFrame1.head()
data2 = dataFrame1.tail()

data_contact = pd.concat([data1,data2],axis =0)

maas = dataFrame1.maas
age = dataFrame1.age

data_h_concat = pd.concat([maas,age],axis=1)

#%%transforming data
dataFrame1["list_comp"]= [each*2 for each in dataFrame1.age]

#%% apply()
def multiply (age):
    return age*2
dataFrame1["apply_metodu"] = dataFrame1.age.apply(multiply)

                     
