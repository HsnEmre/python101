import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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


#aylik satis trendi
aylik_satis=df.resemple('ME')['Satis'].sum()
aylik_satis.plot(kind='Line',title='Aylik Satis Miktarlari')
plt.xlabel('Ay')
plt.ylabel('Satis miktari')
plt.show()



df.plot(kind='scatter',x='Fiyat (TL)',y='Satis',title='Fiyat ve Satis Iliskisi')
z=np.polyfit(df ['Fiyat'].df['Satis'],1)
p=np.poly1d(z)

plt.show()



#cok ise yarar

bins=[0,2000,5000,10000,20000,30000]
labels=['dusuk','orta','yuksek','luks']
#trend lines
df['Fiyat Kategorisi']=pd.cut(df['Fiyat'],bins=bins,labels=labels)
df.groupby('fiyat Kategorisi')['Satis'].sum().plot(kind='bar',title='Fiyat Kategorisine gore toplam satislar')
plt.xlabel('fiyat Kategorisi')
plt.ylabel('Toplam Satis')
plt.show()




