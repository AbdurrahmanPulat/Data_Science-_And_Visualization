# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 16:58:25 2021

@author: DELL
"""

import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) #1*4 vect

print(array.shape)

a = array.reshape(3,5)
print("shape",a.shape)
print("dimension",a.ndim)
print("data type: ",a.dtype.name)
print("size: ",a.size)

print("type",type(a))

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])

zeros = np.zeros((3,4))

zeros[0,0]=5
print(zeros)
np.ones((3,4))

np.empty((2,3))


a= np.arange(10,50,5)
print(a)
  
a = np.linspace (10,50,20)
print(a)

#%%
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)


print(np.sin(a))

print (a<2)

a = np.array([[1,2,3],[4,5,6]])

b = np.array([[1,2,3],[4,5,6]])

#element wisw product

print(a*b)

#matrix product
a.dot(b.T)

print(np.exp(a))

a = np.random.random((5,5))

print(a.sum())
print(a.max())
print(a.min())
  
print(a.sum(axis=0))#sutun toplar
print(a.sum(axis=1)) #satır toplar

print(np.sqrt(a))
print(np.square(a))# a**2


#%%
import numpy as np
array = np.array([1,2,3,4,5,6,7])

print(array[0])

print(array[0:4])

reverse_array = array [::-1]
print(reverse_array)

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1[1,1])

print(array1[:,1])

print( array1[1,1:4])

print([array1[-1, :]])

print([array1[:, -1]])

#%%
#shape manipilation
array = np.array([[1,2,3],[4,5,6],[7,8,9]])

#flatten

a=array.ravel()

array2 = a.reshape(3,3)

arrayT = array2.T

print(arrayT.shape)

array5 = np.array([[1,2],[3,4],[4,5]])


#%%stacking arrays

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])
#vertical
array3 = np.vstack((array1,array2))
#horizontal
array4 = np.hstack((array1,array2))

#%%

liste = [1,2,3,4]

array = np.array(liste)

liste2 = list(array)























