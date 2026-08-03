import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#veriyi hazirlama

data={
    'Ev_buyuklugu':[120,250,175,300,220],
    'fiyat':[30000,40000,50000,60000,70000]
}

df=pd.DataFrame(data)#veriyi df cevvirme

X=df[['Ev_buyuklugu']]
y=df[['fiyat']]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#x ve y beyi test edicegim
#test size ne kadarini test edicem
#random state ne kadar parcalara boluyorum 

#model olustur
model=LinearRegression()
model.fit(X_train,y_train)




# y_pred=model.predict(X_test)
#hata ne kadar kucukse tahmin o kadar iyidir

# mse=mean_squared_error(y_test,y_pred)

# rmse=np.sqrt(mse)

# print(f'Ortalama kare hatasi(mse){rmse}')

ev_buyuklugu=float(input("Lutfen evin buyuklugunu m2 olarak girin :") )
tahmini_fiyat=model.predict([[ev_buyuklugu]])
print(f"Bu Evin Tahmini fiyati:{tahmini_fiyat[0]:.2f}TL")