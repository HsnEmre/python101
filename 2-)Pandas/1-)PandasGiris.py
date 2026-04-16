import pandas as pd


s=pd.Series([10,20,30,40],index=["a","b","c","d"])
print(s)

#multidimensional array
s2={
    'Fiyat':[45,85,46,25],
    'Satis Adet':[5,6,7,8],
    'Kategori':['Roman','Bilim','Cocuk','Tarih']
}
df=pd.DataFrame(s2)
print(df)
print(df.head())
print(df.info())
print(df.describe())
print(df[['Fiyat','Kategori']])

filtre=df[df['Fiyat']>50]
print(filtre)


df['Toplam Gelir']=df['Fiyat'] * df['Satis Adet']
print(df)

df=df.drop('Kategori',axis=1)
print(df)



