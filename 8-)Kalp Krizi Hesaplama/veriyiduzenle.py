import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler

#veriyi yukle
df=pd.read_csv('heart.csv')

# print(df.head())
# print(df.isnull().sum())


#kategorik Sutunlar

categorucal_columns=['ChestPainType','Sex','RestingBP','ExerciseAngina','ST_Slope']

#label ile bu stunlari sayisal hale getir

le=LabelEncoder()
for column in categorucal_columns:
    df[column]=le.fit_transform(df[column])

#kontrol
# print(df.head())

numeric_columns=['Age','RestingBP','Cholesterol','FastingBS','MaxHR','Oldpeak']

#verileri standar hale getir
scaler=StandardScaler()

df[numeric_columns]=scaler.fit_transform(df[numeric_columns])
print(df.head())

df.to_csv('heart_duzenlenmis.csv',index=False)