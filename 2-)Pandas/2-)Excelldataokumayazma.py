import pandas as pd

# Dosyayı oku
df = pd.read_excel('teknolojik_urunler.xlsx') # Yol hatasını çözdüğünü varsayıyorum

# Sütun isimlerindeki gizli boşlukları temizle (Hayat kurtarır)
df.columns = df.columns.str.strip()

print("Sütun İsimleri:", df.columns) # Kontrol için
print(df.head())

# Sütun isminin Excel'de "Fiyat (TL)" olduğundan emin ol
try:
    ortalama_fiyat = df['Fiyat (TL)'].mean()
    print(f"Ortalama Fiyat: {ortalama_fiyat:.2f} TL")
except KeyError:
    print("Hata: 'Fiyat (TL)' sütunu bulunamadı. Mevcut sütunlar:", df.columns)


kategori_bazli_satis=df.groupby('Kategori')['Satış'].sum()
print(kategori_bazli_satis)

#Encok gelir getiren urunu bulma
max_gelir=df.loc[df['Toplam Fiyat (TL)'].idxmax()]
print(f"En Cok Gelit Getiren Urun:\n {max_gelir}")

fiyat_ust_urunler=df[df['Fiyat (TL)']>4000]
print(fiyat_ust_urunler)

fiyat_ust_urunler.to_excel('fiyat_4000_ustu_olanlar.xlsx')