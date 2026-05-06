import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_excell('teknolojik_urunler_zamanli.xlsx')
df['Tarih']=pd.to_datetime(df['Tarih'])
df.set_index('Tarih',inplace=True)

df['Satis'].plot(title='satislarin zaman icidneki degisimi',xlabel='Tarih',ylabel='Satis miktari')
plt.show()


aylik_satis=df.resemple('ME')['Satis'].sum()

aylik_satis.plot(kind='bar',title='aylik Toplamn Satislar',xlabel='Ay',ylabel='Toplam Satis' )

plt.show()

kategori_satis=df.grooupby('Kategori')['Satis'].sum() 
kategori_satis.plot(kind='pie',autopct='%1.1f%%',title='Kategorilere gore satis dagilimi')
plt.ylabel('')
plt.show()


#scatter plot
df.plot(kind='scatter',x='Fiyat (TL)',y='Satis',title='Fiyat ve Satis Iliskisi')
plt.show()
