import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# XOR problemi giriş ve sonuç verileri
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=np.float32)

y = np.array([
    [0],
    [1],
    [1],
    [0]
], dtype=np.float32)

# Basit yapay sinir ağı modeli
model = Sequential([
    Input(shape=(2,)),
    Dense(4, activation="relu"),
    Dense(1, activation="sigmoid")
])

# Modeli derleme
model.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

# Modeli eğitme
model.fit(X, y, epochs=10000, verbose=0)

# Tahmin yapma
tahminler = model.predict(X)

print("Ham tahminler:")
print(tahminler)

print("0 veya 1 olarak tahminler:")
print((tahminler >= 0.5).astype(int))