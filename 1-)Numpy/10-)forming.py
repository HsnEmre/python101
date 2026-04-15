import numpy as np

dizi=np.array([1,2,3,4,5,6])
yeni_dizi=dizi.reshape((2,3))
print(yeni_dizi)

matris=np.array([[1,2],[3,4],[4,5]])
tek_boyut=matris.reshape(-1)
print(tek_boyut)

