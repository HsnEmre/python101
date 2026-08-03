import pandas as pd


#veriyi yukle 
df=pd.read_excel('veri_on_isleme_ve_ozellik_muhendisligi.xlsx')

#eksik gelir verilerini ortalama ile doldurma
df('Gelir').fillna(df['Gelir'].mean(),inplace=True)


print(df)





