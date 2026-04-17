import pandas as pd
import numpy as np

df = pd.read_excel('teknolojik_urunler.xlsx')

#random time span
df['Tarih']=pd.to_datetime(np.random.choice(pd.date_range('2024-01-01','2024-12-31'),size=len(df)))
#show
print(df.head())

df.to_excel('teknolojik_urunler.xlsx',index=False)
print('Veri dosyaya aktarildi')


df['Tarih']=pd.to_datetime(df['Tarih'])
print(df.head())