import pandas as pd

#excell
df=pd.read_excel('teknolojik_urunler_zamanli.xlsx')

print(df)

#date colum convert to datetime format
df['Tarih']=pd.to_datetime(df['Tarih'])
#index
df.set_index('Tarih',inplace=True)
df=df.sort_index()
print(df)

#highest selling product and this sell product

aylik_satis=df.resample('ME')['Satis'].sum()
max_ay=aylik_satis.idxmax()
max_satis_ay=aylik_satis.max()
max_satis_ay_urunler=df[df.index.to_series().between(max_ay-pd.offsets.MonthBegin(1),max_ay)]

print(f"En yuksek satis yapilan ay:{max_ay}-Toplam Satis:{max_satis_ay}")
print(f"o ayda satilan urunler:")
print(max_satis_ay_urunler[['Urun Adi','Satis']])