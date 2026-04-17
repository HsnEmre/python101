import pandas as pd

df = pd.read_excel('teknolojik_urunler1.xlsx')
eksik_veriler=df.isnull()

print(eksik_veriler)

temiz_df=df.dropna
print(temiz_df)

doldurulmus_df=df.fillna(0)
print(doldurulmus_df)

df['Fiyat (TL)']=df['Fiyat (TL)'].astype(float)
print(df.dtypes)


df.insert(2,'Yeni Sutun',range(1,21))
print(df.head())

# df.to_excel('toexcel.xlsx',index=False)
print('Veri Kayit Edildi')


df_dusuk=df.sort_values(by='Fiyat (TL)',ascending=False)
print(df_dusuk)

df_fiyat_ust=df[df['Fiyat (TL)'] > 5000]
print(df_fiyat_ust)

# df_filtre=df[df('Fiyat (TL)' > 5000) & (df['Kategori']=='Mobil Cihazlar')]
# print(df_filtre)

df_secili=df.loc[:,['Urun Adi','Fiyat (TL)']]
print(df_secili)


df_ilk=df.eloc[:5,:]
print(df_ilk)

df_sorgu=df.query('Satis > 10')
print(df_sorgu)


df_kategoriler=df[df['Kategori'].isin(['Bilgisayar','Mobil Cihazlar'])]
print(df_kategoriler)



