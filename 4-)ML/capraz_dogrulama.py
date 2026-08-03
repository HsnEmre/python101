import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df=pd.read_excel('karar_agaci_veri_100.xlsx')
X=df[['yas','kan_basinci','kolestrol']]
y=df[['hastalik']]

# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)


# classiefier=DecisionTreeClassifier()
# classiefier.fit(X_train,y_train)

# y_pred=classiefier.predict(X_test)
# accuracy=accuracy_score(y_test,y_pred)
# print(f"Model Dogruluk Orani: {accuracy}")


classiefier=DecisionTreeClassifier(max_depth=3,min_samples_split=4,min_samples_leaf=2)
classiefier.fit(X,y)

# cross_val_sc=cross_val_score(classiefier,X,y,cv=5)

# print(f"5 katlamali capraz dogrulama skorlari{cross_val_sc}")

print(f"lutfen tahmin icin asagidaki bilgileri giriniz")
yas=int(input("yas: "))
kan_basinci=float(input("Kan basinci: "))
kolestrol=float(input("Kolestrol: ")) 

yeni_veri=pd.DataFrame([yas,kan_basinci,kolestrol],columns=['Yas','Kasn_Basinci','Kolestrol'])

tahmin=classiefier.predict(yeni_veri)

#tahmin sonucunu kullaniciya goster

if tahmin[0]==1:
    print("Hastalik var")
else:
    print("hastalik yok ")    



