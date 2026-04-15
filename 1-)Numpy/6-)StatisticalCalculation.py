import numpy as np

dizi=np.array([1,2,3,4,5,6,7,8,9])
#max value
maks=np.max(dizi)
#min value
min=np.min(dizi)
#array sum
toplam=sum(dizi)
#cluster sum
cl_toplam=np.cumsum(dizi)



#print region
print(maks)
print(min)
print(toplam)
print(cl_toplam)
