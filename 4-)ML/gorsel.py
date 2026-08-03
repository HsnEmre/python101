import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#excell dosyalarini ekle
df=pd.read_excel('karar_agaci_veri_100.xls')
#yas ile hastalik arasindaki iliskiyi gorsellestirme
plt.figure(figsize=(10,6))
sns.gistplot(data=df,x='yas',hue='hastalik',multiple='stack',kde=False)
plt.title('Yas dagilimi ve hastalik durumu')
plt.xlabel('yas')
plt.ylabel('kisi sayisi')
plt.show()



plt.figure(figsize=(10,6))
sns.gistplot(data=df,x='kan_basinci',hue='hastalik',multiple='stack',kde=False)
plt.title('kan_basinci ve hastalik durumu')
plt.xlabel('kan_basinci')
plt.ylabel('kisi sayisi')
plt.show()


plt.figure(figsize=(10,6))
sns.gistplot(data=df,x='kolestrol',hue='hastalik',multiple='stack',kde=False)
plt.title('kolestrol ve hastalik durumu')
plt.xlabel('kolestrol')
plt.ylabel('kisi sayisi')
plt.show()

