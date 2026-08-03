import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Veriyi hazırlama
# data = {
#     "yas": [25, 50, 45, 30, 60],
#     "kan_basinci": [120, 140, 130, 110, 150],
#     "kolestrol": [180, 240, 200, 160, 220],
#     "hastalik": [0, 1, 1, 0, 1]  # 0: Hayır, 1: Evet
# }

df =pd.read_excel('karar_agaci_veri_100.xlsx')

# Bağımsız değişkenler
X = df[["yas", "kan_basinci", "kolestrol"]]

# Tahmin edilecek değişken
y = df["hastalik"]

# Veriyi eğitim ve test olarak ayırma
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model oluşturma
classifier = DecisionTreeClassifier(random_state=42)

# Modeli eğitim verisiyle eğitme
classifier.fit(X_train, y_train)

# Test verisi üzerinde tahmin
y_pred = classifier.predict(X_test)

# Model doğruluğu
accuracy = accuracy_score(y_test, y_pred)

print(f"Gerçek sonuç: {y_test.tolist()}")
print(f"Tahmin edilen sonuç: {y_pred.tolist()}")
print(f"Model doğruluk değeri: {accuracy:.2f}")


yas=int(input("yasinizi giriniz"))
kan_basinci=int(input("kan basinci girin"))
kolestrol=int=(input("kolestrol seviyesi girin"))


kullanici_verisi=pd.DataFrame([[yas,kan_basinci,kolestrol]],columns=['yas','kan_basinci','kolestrol'])
#tahmin olustur
tahmin=classifier.predict([[yas,kan_basinci,kolestrol]])
sonuc="hastalik var" if tahmin[0]==1 else "hastalik yok "
print(f"tahmin:{sonuc}")