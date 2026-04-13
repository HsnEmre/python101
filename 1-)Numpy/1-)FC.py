import numpy as np



#varsayilan dizi olusturma
#creating default squence
dizi=np.array([1,2,3,4,5])
print(dizi)


#otomatik dizi olustur
#creating otomaticly array
dizi1=np.arange(0,10,2) 
print(dizi1)

#belirli bir degeri belirli bir  araliga bol
#dividing a specific value by a specific range
dizi2=np.linspace(0,1,5)
print(dizi2)

#dizi boyutu
#array dimension
boyut=dizi.ndim
#data type
veri_turu=dizi.dtype
print("array squence:",boyut)
print("dizinin turu",veri_turu)