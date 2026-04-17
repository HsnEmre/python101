import pandas as pd

df = pd.read_excel('teknolojik_urunler.xlsx')
gruplar=df.groupby('Kategori')
print(gruplar)

toplam_satis=df.groupby('Kategori')['Fiyat (TL)'].sum()
print(toplam_satis)

toplama_ve_ortalama=df.groupby('Kategori').agg(

    {
        'Satis':'sum',
        'Fiyat (TL)':'mean',
    }
)
print(toplama_ve_ortalama)

en_pahali_urun=df.loc[df.groupby('Kategori')['Fiyat (TL)'].idxmax()]


