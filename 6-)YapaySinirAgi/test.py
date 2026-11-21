import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.layers import Dense  # type: ignore
from tensorflow.keras.models import Sequential  # type: ignore
from tensorflow.keras.optimizers import Adam  # type: ignore

# 1. Veri seti (Eğitim Durumu 23 elemana tamamlandı)
data = {
    'Yaş': [
        25,
        30,
        45,
        50,
        28,
        35,
        40,
        60,
        33,
        48,
        55,
        29,
        39,
        53,
        42,
        37,
        44,
        52,
        58,
        27,
        49,
        36,
        41,
    ],
    'Gelir': [
        2000,
        4000,
        10000,
        3000,
        3500,
        5000,
        8000,
        12000,
        4500,
        9500,
        11000,
        4200,
        6200,
        15000,
        8700,
        3100,
        9800,
        13000,
        7000,
        2900,
        6400,
        5200,
        7200,
    ],
    'Medeni Durum': [
        'Bekar',
        'Evli',
        'Evli',
        'Bekar',
        'Bekar',
        'Evli',
        'Evli',
        'Bekar',
        'Evli',
        'Bekar',
        'Evli',
        'Bekar',
        'Evli',
        'Evli',
        'Bekar',
        'Evli',
        'Bekar',
        'Evli',
        'Bekar',
        'Evli',
        'Evli',
        'Bekar',
        'Evli',
    ],
    'Meslek': [
        'Mühendis',
        'Doktor',
        'Öğretmen',
        'Avukat',
        'Mühendis',
        'Doktor',
        'Avukat',
        'Öğretmen',
        'Doktor',
        'Mühendis',
        'Avukat',
        'Mühendis',
        'Öğretmen',
        'Doktor',
        'Avukat',
        'Mühendis',
        'Öğretmen',
        'Doktor',
        'Avukat',
        'Mühendis',
        'Öğretmen',
        'Avukat',
        'Mühendis',
    ],
    'Eğitim Durumu': [
        'Lisans',
        'Lisans',
        'Yüksek Lisans',
        'Doktora',
        'Lisans',
        'Lisans',
        'Yüksek Lisans',
        'Doktora',
        'Lisans',
        'Yüksek Lisans',
        'Doktora',
        'Lisans',
        'Yüksek Lisans',
        'Doktora',
        'Lisans',
        'Lisans',
        'Yüksek Lisans',
        'Doktora',
        'Yüksek Lisans',
        'Yüksek Lisans',
        'Doktora',
        'Lisans',
        'Lisans',  # Eksik eleman eklendi
    ],
    'Kredi Onayı': [
        0,
        1,
        1,
        0,
        1,
        1,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        1,
        0,
        1,
        1,
        0,
        1,
        0,
        1,
        1,
        0,
    ],
}

df = pd.DataFrame(data)

# 2. Sahte değişkenler (One-Hot Encoding) oluşturma
df_encoded = pd.get_dummies(
    df,
    columns=['Medeni Durum', 'Meslek', 'Eğitim Durumu'],
    drop_first=True,
    dtype=int,
)

# 3. Excel'e aktarma
df_encoded.to_excel('genisletilmisveri.xlsx', index=False)

# 4. Girdi (X) ve Hedef (y) Değişkenlerini Ayırma
X = df_encoded.drop('Kredi Onayı', axis=1)
y = df_encoded['Kredi Onayı']

# 5. Veriyi Eğitim ve Test Olarak Bölme
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. Verileri Ölçeklendirme
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 7. Yapay Sinir Ağı Modelini Kurma
model = Sequential([
    Dense(16, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid'),
])

model.compile(
    optimizer=Adam(learning_rate=0.01),
    loss='binary_crossentropy',
    metrics=['accuracy'],
)

# 8. Modeli Eğitme
model.fit(
    X_train_scaled, y_train, epochs=50, batch_size=4, verbose=0
)  # verbose=0 konsolu temiz tutar

# 9. Test Kümesinde Değerlendirme
y_pred = (model.predict(X_test_scaled) > 0.5).astype(int)
print(f'Test Başarı Oranı (Accuracy): {accuracy_score(y_test, y_pred):.2f}')