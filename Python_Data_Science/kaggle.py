# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 20:41:19 2021

@author: DELL
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool

data = pd.read_csv('pokemon.csv')
data.head()

data.info()
data.corr()
#%%
#corellation map
f,ax =plt.subplots(figsize=(18,18))
sns.heatmap(data.corr(),annot = True, linewidths=.5 , fmt= '.1f', ax=ax)
plt.show()
data.head(10)
data.columns
#%%
data.Speed.plot(kind="line", color="g", label="speed",linewidth=1,alpha=0.5,grid=True, linestyle=":")
data.Defense.plot(kind="line", color="r", label="Defense",linewidth=1,alpha=0.5,grid=True, linestyle="-.")
plt.legend(loc="upper right")
plt.title("line plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

#scatter plot
#x =Attack y= Defense
data.plot(kind="scatter",x="Attack", y="Defense", alpha=0.5,color= "red")
plt.xlabel("Attack")
plt.ylabel("Defense")
plt.title("Attack Defense Scatter Plot")
plt.show()

#histogram
data.Speed.plot(kind="hist", bins= 50, figsize=(15,15))

#clf()
data.Speed.plot(kind="hist",bins=50)
plt.clf()

#%%
#create dictionary and look its keys and values
dictionary ={"Spain":"Madrid","Usa":"Washington"}
print(dictionary.keys())
print(dictionary.values())

# Keys have to be immutable objects like string, boolean, float, integer or tubles
# List is not immutable
# Keys are unique

dictionary["Spain"]= " Barcelona"  # update exiting entry= çıkan girişi güncelle
print(dictionary)

dictionary["France"]= " Paris"     # add new dictionary =  yeni giriş ekle
print(dictionary)

print("France" in dictionary)      # check inculede or not = içerip içermediğini kontrol et

del dictionary["Spain"]
print(dictionary)                  #remove entry with key "spain" = ispanya anahtarını sil

dictionary.clear()
print(dictionary)

# In order to run all code you need to take comment this line = Tüm kodu çalıştırmak için bu satırı yorumlamanız gerekir.
#del dictionary         # delete entire dictionary = Tüm sözlüğü sil     
print(dictionary)       # it gives error because dictionary is deleted  = Sözlük silindiği için hata veriyor

#%%PANDAS


data = pd.read_csv("C:/Users/DELL/myfirstreactproject/pokemon.csv")
series = data["Defense"]       #data["Defense"] =series = Bu bir seridir
data_frame= data[["Defense"]]   # data["defense] = data frame
print(type(data_frame))

# Comparison operator
print(3 > 2)
print(3!=2)
# Boolean operators

print(True and False)
print(True or False)
# 1 - Filtering Pandas data frame

x = data["Defense"]> 200   # There are only 3 pokemons who have higher defense value than 200 = 200'den daha yüksek savunma değerine sahip sadece 3 pokemon var
data[x]

data[np.logical_and(data["Defense"]> 200 , data["Attack"]>100)] #There are only 2 pokemon with defense value higher than 2oo and attack value higher than 100.#2oo'dan daha yüksek savunma değerine ve 100'den daha yüksek saldırı değerine sahip sadece 2 pokemon var.

data[(data['Defense']>200) & (data['Attack']>100)]         # This is the same as the previous line of code. So we can also use '&' for filtering.    # Bu, önceki kod satırıyla da aynıdır. Bu nedenle filtreleme için '&' da kullanabiliriz.



#%% USER DEFINED FUNCTION
# What do we need to know about functions:         

# docstrings: documentation for functions. Example:
# for f():
# """This is docstring for documentation of function f"""
# tuple: sequence of immutable python objects.
# cant modify values
# tuple uses paranthesis like tuble = (1,2,3)
# unpack tuple into several variables like a,b,c = tuple 

#Fonksiyonlar hakkında bilmemiz gerekenler:

# docstrings: işlevler için belgeler. Örnek:
# f() için:
# """Bu, f fonksiyonunun dokümantasyonu için doküman dizisidir"""
# Tuple: değişmez python nesnelerinin dizisi.
# değerleri değiştiremez
# Tuple, tuble = (1,2,3) gibi parantez kullanır
# Tuple'ı a,b,c = tuple gibi çeşitli değişkenlere ayırın

def tuple_ex():
    """return defined tuple"""
    t=(1,2,3)
    return t
a,b,c= tuple_ex()
print(a,b,c)

#%%
#SCOPE
# What we need to know about scope:

# global: defined main body in script
# local: defined in a function
# built in scope: names in predefined built in scope module such as print, len

# Lets make some basic examples

# KAPSAM
# Kapsam hakkında bilmemiz gerekenler:

# global: komut dosyasında tanımlanmış ana gövde
# yerel: bir fonksiyonda tanımlanmış
# yerleşik kapsam: print, len gibi önceden tanımlanmış yerleşik kapsam modülündeki adlar

# Bazı temel örnekler yapalım

# guess prints what    #  tahmin et ne yazdırır
x = 2
def f():
    x =3
    return x
print(x)      # x = 2 global scope = global kapsam
print(f())    # x = 3 local scope =  yerel kapsam



# What if there is no local scope? = Yerel kapsam yoksa ne olur?
x = 5
def f():
    y = 2*x        # there is no local scope x = yerel kapsam yok x
    return y
print(f())         # it uses global scope x  = global kapsam x kullanır
# First local scope searched, then global scope searched, if two of them cannot be found lastly built in scope searched.
#Önce yerel kapsam aranır, ardından global kapsam aranır, bunlardan ikisi bulunamazsa son olarak kapsam içinde yerleşik olarak aranır.

# How can we learn what is built in scope = yerleşik kapsamları nasıl bulabiliriz?# bunlar daha önce python tarafından tanımlanmış belirli kapsamlardır
import builtins
dir (builtins)


#%%NESTED FUNCTION İÇ İÇE FONKSİYONLAR
# function inside function. = Fonksiyon içinde fonksiyon
# There is a LEGB rule that is search local scope, enclosing function, global and built in scopes, respectively. = # Sırasıyla yerel kapsam arama, kapsama işlevi, global ve yerleşik kapsam arama şeklinde bir LEGB kuralı vardır.

def square():
    """ return square of value """
    def add():
        """ add two local variable """
        x = 2
        y = 3
        z = x + y
        return z
    return add()**2
print(square())    

#%%Default Argumans = varsayılan argümanlar

# Default argument example:
# def f(a, b=1):
 #   """ b = 1 is default argument"""
# Flexible argument example:
# def f(*args):
  # """ *args can be one or more"""

#  def f(** kwargs)
# """ **kwargs is a dictionary"""
def f(a, b=1, c=2):
    y =a+b+c
    return y
print(f(5)) # a değeri yerine 5 yazılıyor

# what if we want to change default arguments # ya varsayılan argümanları değiştirmek istersek

print(f(5,4,3))

# flexible arguments *args
def f(*args):
    for i in args:
        print(i)
f(1)
print("")
f(1,2,3,4)

# flexible arguments **kwargs that is dictionary
def f(**kwargs):
    """ print key and value of dictionary"""
    for key, value in kwargs.items():               
        print(key, " ", value)
f(country = 'spain', capital = 'madrid', population = 123456)


#%%
 #User Defined Function(long way)
def square(x):
     return x**2
print(square(5))

#User dDefined Function(short way)

square = lambda x: x**2 #where x is name of argument
print(square(4))

tot = lambda x,y,z : x+y+z     #where x,y,z is name of argument
print(tot(1,2,3))      


#%%ANONYMOUS FUNCTİON
#Like lambda function but it can take more than one arguments.

#map(func,seq) : applies a function to all the items in a list

number_list = [1,2,3]
y = map(lambda x : x**2, number_list)      # map fonksiyonu bize listedeki elemanların tek tek karelerini hesaplamamızda yardımcı oluyor yani lambda fonksiyonunu her bir parametre için kullanmamızı sağlıyor
print(list(y))

#%%# iteration example
name = "ronaldo"
it = iter(name)
print(next(it))    # print next iteration
print(*it)         # print remaining iteration

#%% zip example
list1 = [1,2,3,4]
list2 = [5,6,7,8]
z = zip(list1, list2)
print(z)
z_list = list(z)
print(z_list)

un_zip = zip(*z_list)
un_list1,un_list2 =list(un_zip) #un_list return tuple
print(un_list1)
print(un_list2)
print(type(un_list2))

#%%
# LIST COMPREHENSİON
# One of the most important topic of this kernel
# We use list comprehension for data analysis often.
# list comprehension: collapse for loops for building lists into a single line
# Ex: num1 = [1,2,3] and we want to make it num2 = [2,3,4]. This can be done with for loop. However it is unnecessarily long. We can make it one line code that is list comprehension.

num1 = [1,2,3]
num2 = [i+1 for i in num1]
print(num2)


# [i + 1 for i in num1 ]: list of comprehension
# i +1: list comprehension syntax
# for i in num1: for loop syntax
# i: iterator
# num1: iterable object

# [num1'deki i için i + 1): kavrama listesi
# i +1: liste anlama sözdizimi
# num1'deki i için: döngü sözdizimi için
# i: yineleyici
# num1: yinelenebilir nesne

num1 = [5,10,15]
num2 =[i**2 if i==10 else i-5 if i < 7 else i +5 for i in num1]
print(num2)
 #%%
import pandas as pd
data = pd.read_csv('pokemon.csv')
data.head()
data.tail()

data.columns # columns gives column names of features    # başlık isimleri

data.shape      # shape gives number of rows and columns in a tuble  # satır ve sütun sayısı

# info gives data type like dataframe, number of sample or row, number of feature or column, feature types and memory usage
data.info()

# For example lets look frequency of pokemom types # Örneğin pokemon türlerinin sıklığına bakalım

print(data["Type 1"].value_counts(dropna = False))


#%%
# EXPLORATORY DATA ANALYSIS
# value_counts(): Frequency counts
# outliers: the value that is considerably higher or lower from rest of the data

# Lets say value at 75% is Q3 and value at 25% is Q1.
# Outlier are smaller than Q1 - 1.5(Q3-Q1) and bigger than Q3 + 1.5(Q3-Q1). (Q3-Q1) = IQR
# We will use describe() method. Describe method includes:
# count: number of entries
# mean: average of entries
# std: standart deviation
# min: minimum entry
# 25%: first quantile
# 50%: median or second quantile
# 75%: third quantile
# max: maximum entry

# KEŞİF VERİ ANALİZİ
# value_counts(): Frekans sayıları
# aykırı değerler: verilerin geri kalanından önemli ölçüde yüksek veya düşük olan değer

# Diyelim ki %75'teki değer Q3 ve %25'teki değer Q1.
# Outlier, Q1 - 1.5(Q3-Q1)'den küçük ve Q3 + 1.5(Q3-Q1)'den daha büyük. (Q3-Q1) = IQR
# tarif() yöntemini kullanacağız. Açıklama yöntemi şunları içerir:
# sayı: giriş sayısı
# ortalama: girişlerin ortalaması
# standart: standart sapma
# dak: minimum giriş
# %25: ilk nicelik
# %50: medyan veya ikinci nicelik
# %75: üçüncü nicelik
# max: maksimum giriş


# What is quantile?

# 1,4,5,6,8,9,11,12,13,14,15,16,17
# The median is the number that is in middle of the sequence. In this case it would be 11.

# The lower quartile is the median in between the smallest number and the median i.e. in between 1 and 11, which is 6.

# The upper quartile, you find the median between the median and the largest number i.e. between 11 and 17, which will be 14 according to the question above.


# quantile nedir?

# 1,4,5,6,8,9,11,12,13,14,15,16,17
# Medyan, dizinin ortasındaki sayıdır. Bu durumda 11 olur.

# Alt çeyrek, en küçük sayı ile medyan arasındaki medyandır, yani 1 ile 11 arasında, yani 6'dır.

# Üst çeyrek, medyanı medyan ile en büyük sayı arasında yani yukarıdaki soruya göre 14 olacak olan 11 ile 17 arasında buluyorsunuz.

#%%VISUAL EXPLORATORY DATA ANALYSIS
#Box plots: visualize basic statistics like outliers, min/max or quantiles
#Kutu grafikleri: aykırı değerler, min/maks veya nicelikler gibi temel istatistikleri görselleştirin

# For example: compare attack of pokemons that are legendary  or not
# Black line at top is max
# Blue line at top is 75%
# Green line is median (50%)
# Blue line at bottom is 25%
# Black line at bottom is min
# There are no outliers

data.describe()

data.boxplot(column= "Attack", by="Legendary")


#%%TIDY DATA
#We tidy data with melt(). Describing melt is confusing. Therefore lets make example to understand it.
#DÜZENLİ VERİLER
#Verileri melt() ile düzenliyoruz. Erimeyi tanımlamak kafa karıştırıcıdır. Bu yüzden anlamak için örnek yapalım.

# Firstly I create new data from pokemons data to explain melt nore easily. = # İlk olarak melt nore'u kolayca açıklamak için pokemon verilerinden yeni veriler oluşturuyorum.
    


data_new = data.head()
data_new

# lets melt
# id_vars = what we do not wish to melt
# value_vars = what we want to melt

# eritelim
# id_vars = eritmek istemediğimiz şey
# value_vars = eritmek istediğimiz şey

melted = pd.melt(frame= data_new, id_vars="Name", value_vars=["Attack","Defense"])
melted



#%%PIVOTING DATA
#Reverse of melting.

# Index is name
# I want to make that columns are variable
# Finally values in columns are value

# İndeks isimdir
# Bu sütunları değişken yapmak istiyorum
# Son olarak sütunlardaki değerler değerdir
melted.pivot(index = 'Name', columns = 'variable',values='value')

#%%CONCATENATING DATA
#We can concatenate two dataframe =#İki veri çerçevesini birleştirebiliriz

# Firstly lets create 2 data frame # Öncelikle 2 data frame oluşturalım
data1 = data.head()
data2= data.tail()
conc_data_row =pd.concat([data1,data2],axis=0,ignore_index= True)   #axis=0 verileri yatay eksende sıralar
conc_data_row

data1 =data["Attack"].head()       
data2 =data["Defense"].head()

conc_data_col = pd.concat([data1,data2],axis=1) #verileri dikey eksende sıralar

conc_data_col


#%%
# DATA TYPES There are 5 basic data types: object(string),boolean, integer, float and categorical. We can make conversion data types like from str to categorical or from int to float Why is category important:

# make dataframe smaller in memory can be utilized for anlaysis especially for sklearn.

# VERİ TÜRLERİ 5 temel veri türü vardır: nesne(string), boolean, tamsayı, kayan nokta ve kategorik. str'den kategoriye veya int'den float'a gibi dönüşüm veri türlerini yapabiliriz. Kategori neden önemlidir:

# veri çerçevesini bellekte küçültme, analiz için özellikle sklearn için kullanılabilir.

# lets convert object(str) to categorical and int to float.
data['Type 1'] = data['Type 1'].astype('category')
data['Speed'] = data['Speed'].astype('float')

# As you can see Type 1 is converted from object to categorical = # Gördüğünüz gibi Type 1 nesneden kategoriye dönüştürülür

# And Speed ,s converted from int to float =# Ve Hız, int'den float'a dönüştürülür
data.dtypes

#%%MISSING DATA and TESTING WITH ASSERT
# If we encounter with missing data, what we can do:

# leave as is
# drop them with dropna()
# fill missing value with fillna()
# fill missing values with test statistics like mean
# Assert statement: check that you can turn on or turn off when you are done with your testing of the program
 

# EKSİK VERİLER VE ASSERT İLE TEST EDİLMESİ
# Eksik verilerle karşılaşırsak ne yapabiliriz:

# olduğu gibi bırak
# onları dropna() ile bırak
# eksik değeri fillna() ile doldurun
# ortalama gibi test istatistikleri ile eksik değerleri doldurun
# Assert deyimi: programı test etmeniz bittiğinde açıp kapatabileceğinizi kontrol edin



















data.info()

# Lets chech Type 2
data["Type 2"].value_counts(dropna =False)
# As you can see, there are 386 NAN value (Gördüğünüz gibi 386 NAN değeri var)



# Lets drop nan values (nan değerlerini bırakalım)
data1=data   # also we will use data to fill missing value so I assign it to data1 variable  #ayrıca eksik değeri doldurmak için verileri kullanacağız, bu yüzden onu data1 değişkenine atadım
data1["Type 2"].dropna(inplace = True)  # inplace = True means we do not assign it to new variable. Changes automatically assigned to data # inplace = True, onu yeni değişkene atamadığımız anlamına gelir. Verilere otomatik olarak atanan değişiklikler
# So does it work ?


#  Lets check with assert statement
# Assert statement:
assert 1==1 # return nothing because it is true

# In order to run all code, we need to make this line comment # Kodun tamamını çalıştırabilmemiz için bu satırın yorumunu yapmamız gerekiyor.

# assert 1==2 # return error because it is false  # assert 1==2 # false olduğu için hata döndür

assert  data['Type 2'].notnull().all() # returns nothing because we drop nan values =# nan değerlerini düşürdüğümüz için hiçbir şey döndürmez


data["Type 2"].fillna('empty',inplace = True)

assert  data['Type 2'].notnull().all() # returns nothing because we do not have nan values= #nan değerlerimiz olmadığı için hiçbir şey döndürmez


# # With assert statement we can check a lot of thing. For example
# assert data.columns[1] == 'Name'
# assert data.Speed.dtypes == np.int

## Assert deyimi ile bir çok şeyi kontrol edebiliriz. Örneğin
# assert data.columns[1] == 'Name'
# assert data.Speed.dtypes == np.int

#%%PANDAS FOUNDATION


# REVİEW of PANDAS
# As you notice, I do not give all idea in a same time. Although, we learn some basics of pandas, we will go deeper in pandas.

# single column = series
# NaN = not a number
# dataframe.values = numpy


# PANDAS İNCELEMESİ
# Fark ettiğiniz gibi tüm fikirleri aynı anda vermiyorum. Pandasın bazı temellerini öğrenmiş olsak da , pandasda daha derine ineceğiz.

# tek sütun = seri
# NaN = değer yok
# dataframe.values ​​= numpy

# data frames from dictionary
import pandas as pd


country = ["spain","France"]
population =["11","12"]
list_label = ["country","population"]
list_col = [country,population]
zipped= list(zip(list_label,list_col))
data_dict= dict(zipped)
df= pd.DataFrame(data_dict)
df
# listeden başlayarak önce dictionary oluşturduk daha sonra dataframe oluşturduk

# add new columns # yeni sütun ekleme
df["capital"]= ["madrid","paris"]
df

#Broadcasting entire column 
df["income"] = 0 
df


#%%# Plotting all data 
data1 = data.loc[:,["Attack","Defense","Speed"]]
data1.plot()
# it is confusing


#%%
# subplots
data1.plot(subplots = True)
plt.show()
#%%
# scatter plot  
data1.plot(kind = "scatter",x="Attack",y = "Defense")
plt.show()
#%%
# hist plot  
data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True)
#%%
# histogram subplot with non cumulative and cumulative
fig, axes = plt.subplots(nrows=2,ncols=1)
data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True,ax = axes[0])
data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True,ax = axes[1],cumulative = True)
plt.savefig('graph.png')
plt
#%%

# INDEXING PANDAS TIME SERIES
# datetime = object
# parse_dates(boolean): Transform date to ISO 8601 (yyyy-mm-dd hh:mm:ss ) format


# PANDAS ZAMAN SERİSİ ENDEKSİ
# tarihsaat = nesne
# parse_dates(boolean): Tarihi ISO 8601 (yyyy-aa-gg ss:dd:ss ) biçimine dönüştürün

time_list = ["1992-03-08","1992-04-12"]
print(type(time_list[1])) # As you can see date is string # Gördüğünüz gibi tarih string
# however we want it to be datetime object ## ancak bunun datetime nesnesi olmasını istiyoruz
datetime_object = pd.to_datetime(time_list)
print(type(datetime_object))

# close warning
import warnings
warnings.filterwarnings("ignore")
# In order to practice lets take head of pokemon data and add it a time list ## Pratik yapmak için pokemon verilerinin başını alıp bir zaman listesi ekleyelim
data2 = data.head()

#%%



date_list = ["1992-01-10","1992-02-10","1992-03-10","1993-03-15","1993-03-16"]
datetime_object = pd.to_datetime(date_list)
data2["date"] = datetime_object
# lets make date as index = indeks olarak tarih yapalım
data2= data2.set_index("date")
data2 

# Now we can select according to our date index # Artık tarih dizinimize göre seçim yapabiliriz
print(data2.loc["1993-03-16"])
print(data2.loc["1992-03-10":"1993-03-16"])


#RESAMPLING PANDAS TIME SERIES
# Resampling: statistical method over different time intervals
# Needs string to specify frequency like "M" = month or "A" = year
# Downsampling: reduce date time rows to slower frequency like from daily to weekly
# Upsampling: increase date time rows to faster frequency like from daily to hourly
# Interpolate: Interpolate values according to different methods like ‘linear’, ‘time’ or index’
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.interpolate.html

#PANDAS ZAMAN SERİSİNİN YENİDEN ÖRNEKLENMESİ
# Yeniden örnekleme: farklı zaman aralıklarında istatistiksel yöntem
# "M" = ay veya "A" = yıl gibi bir sıklık belirtmek için dize gerekiyor
# Altörnekleme: tarih saat satırlarını günlükten haftalık gibi daha yavaş sıklığa düşürün
# Örnekleme: tarih saat satırlarını günlükten saatlik gibi daha hızlı sıklığa yükseltin
# Interpolate: Değerleri 'doğrusal', 'zaman' veya dizin' gibi farklı yöntemlere göre enterpolasyon yapın
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.interpolate.html


# We will use data2 that we create at previous part ## Bir önceki bölümde oluşturduğumuz data2'yi kullanacağız
data2.resample("A").mean()

# We will use data2 that we create at previous part # bir önceki bölümde oluşturduğumuz data2 yi kullanacağız

data2.resample("M").mean()

# In real life (data is real. Not created from us like data2) we can solve this problem with interpolate =  # Gerçek hayatta (veriler gerçektir. data2 gibi bizden yaratılmamışlardır) bu sorunu enterpolasyon ile çözebiliriz.
# We can interpolete from first value = # İlk değerden enterpolasyon yapabiliriz.


data2.resample("M").first().interpolate("linear")

# Or we can interpolate with mean()
data2.resample("M").mean().interpolate("linear")

#%%MANIPULATING DATA FRAMES WITH PANDAS

data = pd.read_csv('pokemon.csv')
data= data.set_index("#")
data.head()


data["HP"][1] #OR
data.HP[1]

# using loc accessor
data.loc[1,["HP"]]


# Selecting only some columns
data[["HP","Attack"]]


# Difference between selecting columns: series and dataframes = # Sütun seçme arasındaki fark: seriler ve veri çerçeveleri
print(type(data["HP"]))     # series
print(type(data[["HP"]]))   # data frames

# Slicing and indexing series
data.loc[1:10,"HP":"Defense"]   # 10 and "Defense" are inclusive

# Reverse slicing 
data.loc[10:1:-1,"HP":"Defense"] 

# From something to end
data.loc[1:10,"Speed":]


#%%
# FILTERING DATA FRAMES = VERİ ÇERÇEVELERİNİN FİLTRELENMESİ
# Creating boolean series Combining filters Filtering column based others = # Boolean serisi oluşturma Filtreleri birleştirme Sütun bazında diğerlerini filtreleme
# Creating boolean series
boolean = data.HP > 200
data[boolean]

# Combining filters
first_filter = data.HP > 150
second_filter = data.Speed > 35
data[first_filter & second_filter]
    

# Filtering column based others
data.HP[data.Speed<15]

#%%DÖNÜŞÜM VERİLERİ
# Düz PYTHON işlevleri
# Lambda işlevi: her öğeye isteğe bağlı python işlevi uygulamak için
# Diğer sütunları kullanarak sütun tanımlama

# TRANSFORMING DATA
# Plain python functions
# Lambda function: to apply arbitrary python function to every element
# Defining column using other columns

data.HP.apply(lambda n : n/2)


# Defining column using other columns  # farklı bir sütun oluşturmak istediğimizde
data["total_power"] = data.Attack + data.Defense
data.head()
#%%
# INDEX OBJECTS AND LABELED DATA İNDEKS NESNELERİ VE ETİKETLİ VERİLER

# index: sequence of label   = # ındex: etiket dizisi
# our index name is this:
print(data.index.name)
# lets change it = değiştirelim
data.index.name = "index_name"
data.head()

# Overwrite index    # ındex in  üzerine yaz

# if we want to modify index we need to change all of them. # indeksi değiştirmek istiyorsak hepsini değiştirmemiz gerekiyor.
data.head()
# first copy of our data to data3 then change index  # önce verilerimizin data3'e kopyalanması, ardından ındex i değiştirme
data3 = data.copy()
# lets make index start from 100. It is not remarkable change but it is just example  # indeksi 100'den başlatalım. Dikkate değer bir değişiklik değil, sadece örnek
data3.index = range(100,900,1)
data3.head()

#%%HIERARCHICAL INDEXING Hiyerarşik indeksleme
# Setting indexing # İndekslemeyi ayarlama

# lets read data frame one more time to start from beginning  =# baştan başlamak için veri çerçevesini bir kez daha okuyalım
data = pd.read_csv('pokemon.csv')
data.head() 
# As you can see there is index. However we want to set one or more column to be index  # Gördüğünüz gibi indeks var. Ancak bir veya daha fazla sütunu dizin olarak ayarlamak istiyoruz.

# Setting index : type 1 is outer type 2 is inner index # Ayar indeksi : tip 1 dış tip 2 iç indekstir
data1 = data.set_index(["Type 1","Type 2"]) 
data1.head(100)
# data1.loc["Fire","Flying"] # howw to use indexes  # data1.loc["Fire","Flying"] # dizinlerin nasıl kullanılacağı

#%%
# PIVOTING DATA FRAMES
# pivoting: reshape tool
dic = {"treatment":["A","A","B","B"],"gender":["F","M","F","M"],"response":[10,45,5,9],"age":[15,4,72,65]}
df = pd.DataFrame(dic)
df
# pivoting
df.pivot(index="treatment",columns = "gender",values="response")
#%%
# STACKING and UNSTACKING DATAFRAME    İSTİFLEME ve İSTİFTEN ÇIKARMA VERİ ÇERÇEVESİ

# deal with multi label indexes    # çoklu etiket ındexleriyle ilgilen
# level: position of unstacked index   # seviye: yığınlanmamış ındex konumu

# swaplevel: change inner and outer level index position # takas düzeyi: iç ve dış düzey ındex konumunu değiştir
df1 = df.set_index(["treatment","gender"])
df1
# lets unstack it   # kaldıralım


# level determines indexes # seviye indeksleri belirler
df1.unstack(level=0)

df1.unstack(level=1)

# change inner and outer level index position   # iç ve dış seviye ındex konumunu değiştir
df2 = df1.swaplevel(0,1)
df2


#%%MELTING DATA FRAMES
# Reverse of pivoting
df

# df.pivot(index="treatment",columns = "gender",values="response")   # df.pivot(index="tedavi",sütunlar = "cinsiyet",değerler="yanıt")
pd.melt(df,id_vars="treatment",value_vars=["age","response"])


#%%CATEGORICALS AND GROUPBY¶
# We will use df
df

# according to treatment take means of other features       # tedaviye göre diğer özelliklerden yararlanın


df.groupby("treatment").mean()   # mean is aggregation / reduction method     # ortalama, toplama/indirgeme yöntemidir
# there are other methods like sum, std,max or min  # sum, std, max veya min gibi başka yöntemler de var

# we can only choose one of the feature # özelliklerden sadece birini seçebiliriz
df.groupby("treatment").age.max() 


# Or we can choose multiple features  # Veya birden fazla özellik seçebiliriz
df.groupby("treatment")[["age","response"]].min()

#%%
plt.style.available # istediğimiz seborn görselleştirme biçimini ekleyebiliriz 












































