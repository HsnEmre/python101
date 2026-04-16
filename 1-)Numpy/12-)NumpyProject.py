import numpy as np

# Her dizi 7 elemanlı olmalı
kitap_fiyatlari = np.array([25, 45, 20.35, 50, 40, 30, 35]) 
satis_adetleri = np.array([100, 150, 200, 120, 130, 80, 110])
kategoriler = np.array(["Roman", "Bilim", "Cocuk", "Tarih", "Roman", "Bilim", "Cocuk"])

toplam_gelir = kitap_fiyatlari * satis_adetleri

print("Toplam Gelir Dizisi:", toplam_gelir)
print("Kategoriler:", kategoriler)

ortalama_fiyat = np.mean(kitap_fiyatlari)
max_fiyat = np.max(kitap_fiyatlari)
min_fiyat = np.min(kitap_fiyatlari)

print(f"\nOrtalama Fiyat: {ortalama_fiyat:.2f}")
print(f"Maksimum Fiyat: {max_fiyat}")
print(f"Minimum Fiyat: {min_fiyat}")

romanlar=kitap_fiyatlari[kategoriler=="Roman"]
print("Roman :",romanlar)

roman_satislari=satis_adetleri[kategoriler=="Roman"]
print("Roman Satis",roman_satislari)

roman_toplam_satis=np.sum(romanlar * roman_satislari)
print("roman toplam Satis",roman_toplam_satis)

#reshaping
veri=np.array([kitap_fiyatlari,satis_adetleri])
veri_reshaped=np.reshape(veri,(2,7))
print(veri_reshaped)