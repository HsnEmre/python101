import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import StandardScaler

# 1. Veri seti
X = np.array([
    [25, 2000],
    [30, 4000],
    [45, 10000],
    [50, 3000]
])

y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# 2. Veriyi ölçeklendir
scaler = StandardScaler()
X_Scaled = scaler.fit_transform(X)

# 3. Model mimarisi
model = Sequential()
model.add(Dense(5, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Düzeldi: learning_rate küçük harf yapıldı
optimizer = Adam(learning_rate=0.005)
model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])

# 4. Eğit
model.fit(X_Scaled, y, epochs=200, verbose=0)

# Düzeldi: Tahmin yaparken de ölçeklenmiş veri (X_Scaled) verilmeli
tahminleme = model.predict(X_Scaled)
print('Eğitim verisi tahminleri:\n', tahminleme)

# 5. Kullanıcıdan yeni girdi alma
# while True:
#     try:
#         yas = float(input('\nYaş girin (Çıkış için Ctrl+C): '))
#         gelir = float(input('Gelir girin: '))

#         # Yeni veriyi diziye çevir ve EĞİTİLMİŞ SCALER ile dönüştür
#         user_data = np.array([[yas, gelir]])
#         user_data_scaled = scaler.transform(user_data)

#         # Tahmin al
#         prediction = model.predict(user_data_scaled, verbose=0)
#         print(f'Tahmin sonucu (Olasılık): {prediction[0][0]:.4f}')
#         print(f'Sınıf: {1 if prediction[0][0] >= 0.5 else 0}')
#     except KeyboardInterrupt:
#         print("\nÇıkış yapıldı.")
#         break


# while True:
#     user_input_1=float(input('yasinizi giriniz'))
#     user_input_2=float(input('maasinizi giriniz'))

#     #kullanicidan alinann  verileri modele uygun hale getirme
#     user_data=np.array([[user_input_1,user_input_2]])

#     #girdileri olceklendirme
#     user_data_scaled=scaler.transform(user_data)
#     #tahmin olustur
#     prediction=model.predict(user_data_scaled)
#     #sonucu yazdiralim
#     print(f'tahmin sonucu:{prediction[0][0]}:.4f')


while True:
    user_input_1=float(input('yasinizi giriniz'))
    user_input_2=float(input('maas giriniz'))
    user_input_3=input('medeni durumunuzu giriniz(bekar/evli)')
    user_input_4=input('meslek?')
    user_input_5=input('egitim durumunuzu giriniz(lisan,onlisans,ise)')


    user_data=pd.DataFrame(
        {
            'yas':[user_input_1],
            'gelir':[user_input_2],
            'medeni durum'+user_input_3:[1],
            'meslek'+user_input_4:[1],
            'egitim durum'+user_input_5:[1]
        }
    )

    user_Data=user_data.reindex(columns=df.drop('Kredi Onayi',axis=1).columns,fill_value=0)
    #veriyi olceklendirme
    user_data_scaled=scaler.transform(user_Data)
    #tahminleme
    prdiction=model.predict(user_data_scaled)
    print(f'tahminleme sonucu:{prediction[0][0]:.4f}')