import numpy as np

# 1. Tek boyutlu dizi birleştirme
dizi1 = np.array([1, 2, 3])
dizi2 = np.array([4, 5, 6])
bd = np.concatenate((dizi1, dizi2))
print("Birleşik Dizi:\n", bd)

# 2. Çok boyutlu dizi birleştirme (hstack)
dizi_a = np.array([[1, 2, 3], [4, 5, 6]])
dizi_b = np.array([[7, 8, 9], [10, 11, 12]])

bd2 = np.hstack((dizi_a, dizi_b)) # dizi2 yerine dizi_b kullanıldı
print("\nYatay Birleşmiş (hstack):\n", bd2)

# 3. Bölme (split)
# Satır üzerinden 2'ye böler (2 satır olduğu için sorunsuz çalışır)
bd3 = np.split(dizi_a, 2)
print("\nSatırdan Bölünmüş:\n", bd3)

# 4. Çok boyutlu split (hsplit)
# bd2'yi kullanıyoruz çünkü o 6 sütunlu, 2'ye veya 3'e tam bölünür
bd4 = np.hsplit(bd2, 2) 
print("\nSütundan Bölünmüş (hsplit):\n", bd4)