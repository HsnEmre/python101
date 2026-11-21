
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Excel dosyasını okuma
df = pd.read_excel('kredi_onay_verisi_1000.xlsx')

# Sütun seçimi
X = df[['Yas', 'Gelir']].values
y = df['Kredi Onayi'].values 

# Veriyi test ve eğitim olarak bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=43)

# SMOTE ile veri dengesini sağlama
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

# Veriyi ölçeklendirme
scaler = StandardScaler()
X_train_smote_scaled = scaler.fit_transform(X_train_smote)
X_test_scaled = scaler.transform(X_test)

# --- Random Forest Modeli ---
model = RandomForestClassifier(random_state=42)
model.fit(X_train_smote_scaled, y_train_smote)

y_pred = model.predict(X_test_scaled)
rf_accuracy = accuracy_score(y_test, y_pred)
print(f'Random Forest Test Dogruluk Orani: %{rf_accuracy * 100:.2f}')

# --- Yapay Sinir Ağları (YSA) Modeli ---
nn_model = Sequential()
nn_model.add(Dense(16, input_dim=2, activation='relu'))
nn_model.add(Dense(1, activation='sigmoid'))

# Modeli derleme (learning_rate ve metrics düzeltildi)
optimizer = Adam(learning_rate=0.001)
nn_model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])

# Modeli eğitme (verbose düzeltildi)
nn_model.fit(X_train_smote_scaled, y_train_smote, epochs=100, batch_size=32, verbose=1)

# YSA tahminleme ve doğrulama (y_pred_nn değişken adı düzeltildi)
y_pred_nn = (nn_model.predict(X_test_scaled) > 0.5).astype('int32')
nn_accuracy = accuracy_score(y_test, y_pred_nn)

print(f'Yapay Sinir Agi Test Dogruluk Orani: %{nn_accuracy * 100:.2f}')