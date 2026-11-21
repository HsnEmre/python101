import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Excel dosyasını oku
df = pd.read_excel(
    r'D:\Egitim & Udemy\python101\9-)Deprem\deprem.xlsx'
)

# İlk 5 satırı göster
print("İlk 5 satır:")
print(df.head(5))

# Veri seti bilgisi
print("\nVeri seti bilgisi:")
df.info()

# Temel istatistikler
print("\nTemel istatistiksel özet:")
print(df.describe())

# Eksik değerleri kontrol et
print("\nSütunlardaki eksik değer sayıları:")
print(df.isnull().sum())

# Tarih ve saat sütunlarını birleştir
df['TarihSaat'] = pd.to_datetime(
    df['Tarih'].astype(str).str.strip()
    + ' '
    + df['Saat'].astype(str).str.strip(),
    format='%Y.%m.%d %H:%M:%S'
)

# Eski tarih ve saat sütunlarını kaldır
df.drop(columns=['Tarih', 'Saat'], inplace=True)

print("\nGüncellenmiş veri tipleri:")
print(df.dtypes)

# ML sütununu sayısal değerlere dönüştür
# Sayıya çevrilemeyen değerler NaN olur
df['ML'] = pd.to_numeric(df['ML'], errors='coerce')

print("\nML sütunundaki eksik değer sayısı:")
print(df['ML'].isnull().sum())

# ML değeri eksik olan satırları kaldır
df_clean = df.dropna(subset=['ML']).copy()

print("\nTemizlenmiş veri boyutu (satır, sütun):")
print(df_clean.shape)

# Temizlenen verilerdeki depremleri günlere göre say
if df_clean.empty:
    print("\nGrafik oluşturmak için veri kalmadı.")
else:
    tarihler = df_clean['TarihSaat'].dt.date

    plt.figure(figsize=(12, 6))

    sns.countplot(
        x=tarihler,
        order=sorted(tarihler.unique()),
        color='steelblue'
    )

    # plt.xticks(rotation=45, ha='right')
    # plt.title('Günlere Göre Deprem Sayısı')
    # plt.xlabel('Tarih')
    # plt.ylabel('Deprem Sayısı')
    # plt.tight_layout()
    # plt.show()

    #depremin buyukluk dagilimi

    plt.figure(figsize=(8,6))
    sns.histplot(df_clean['ML'],bins=20,kde=True,color='skyblue')
    plt.title('deprem buyukluk dagilim')
    plt.xlabel('buyukluk (ML)')
    plt.ylabel('Frekans')
    plt.show()


    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df_clean,x='Derinlik(km)',hue='Yer',palette='deep')
    plt.title('derinligine gore deprem buyuklukleri')
    plt.xlabel('Derinlik')
    plt.ylabel('buyukluk(km)')
    plt.legend(bbox_to_anchor=(1.05,1),loc="upper left")
    plt.tight_layout()
    plt.show()