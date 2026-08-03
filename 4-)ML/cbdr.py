import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Veriyi hazırlama
data = {
    'Ev_buyuklugu': [120, 250, 175, 300, 220],
    'oda_sayisi': [3, 4, 5, 6, 7],
    'fiyat': [30000, 40000, 50000, 60000, 70000]
}

df = pd.DataFrame(data)

# Bağımsız değişkenler
X = df[['Ev_buyuklugu', 'oda_sayisi']]

# Tahmin edilecek değişken
y = df['fiyat']

# Eğitim ve test verilerini ayırma
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model oluşturma ve eğitme
model = LinearRegression()
model.fit(X_train, y_train)

# Modeli test etme
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"Ortalama karekök hata (RMSE): {rmse:.2f} TL")

# Kullanıcıdan veri alma
ev_buyuklugu = float(
    input("Lütfen evin büyüklüğünü m² olarak girin: ")
)

oda_sayisi = int(
    input("Lütfen oda sayısını girin: ")
)

# Tahmin verisini sütun isimleriyle hazırlama
yeni_ev = pd.DataFrame({
    'Ev_buyuklugu': [ev_buyuklugu],
    'oda_sayisi': [oda_sayisi]
})

tahmini_fiyat = model.predict(yeni_ev)[0]

print(f"Bu evin tahmini fiyatı: {tahmini_fiyat:.2f} TL")