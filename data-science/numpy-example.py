# https://numpy.org/
import numpy as np

from numpy import random


print(np.__version__)


arrA = np.array([[[1,2,3,4,5], [10,20,30,40,50], [100,200,300,400,500]]])

print(type(arrA))

print(arrA.ndim)
#print(arrA[0][2][4])

#for i in range(len(arrA[0][2])):
  #print(arrA[0][2][i])


arrB = np.array([1,2,3,4,5])
random.shuffle(arrB)
print(arrB)
random.shuffle(arrA[0][2])
print(arrA[0][2])
