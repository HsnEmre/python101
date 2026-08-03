import pandas as pd
from sklearn.preprocessing import LabelEncoder

#veriyi yukle 
df=pd.read_excel('veri_on_isleme_ve_ozellik_muhendisligi.xlsx')

#eksik gelir verilerini ortalama ile doldurma
df('Gelir').fillna(df['Gelir'].mean(),inplace=True)


print(df)


le=LabelEncoder()
df['Cinsiyet']=le.fit_transform(df['cinsiyet'])
print(df)




