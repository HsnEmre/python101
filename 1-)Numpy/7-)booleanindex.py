import numpy as np

# Sorun buradaydı: np.array() içine almalısın
dizi = np.array([10,20,30,40,50,60,70,80,90,100,110,1,2,3,4,6,23,5,234,123])

# Artık bu işlem hata vermez
boolean_mask = dizi > 50
print(boolean_mask)

# Filtrelenmiş elemanlar
secilmis = dizi[boolean_mask]
print(secilmis)

#coklu eleme
bm=(dizi>30)&(dizi<100)
print([bm])