import numpy as np

array1=np.array([1,2,3,4,5])
array2=np.array([14,22,33,41,51])

sum=array1+array2
subtraction=array1-array2
impact=array1*array2
divide=array1/array2
print(sum)
print(subtraction)
print(impact)
print(divide)


#Sum Function
toplam=np.sum(array1)
print(toplam)
#impact func
carpim=np.prod(array1)
print(carpim)
#SQRT
kok=np.sqrt(array1)
print(array1)

#arithmetich mean
ortalama=np.mean(array1)
print(ortalama)

#median
medyanal=np.median(array1)
print(medyanal)

#standard deviation
standartsapma=np.std(array1)
print(standartsapma)