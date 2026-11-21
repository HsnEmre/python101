import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

klasor = Path(__file__).parent
df = pd.read_csv(klasor / 'heart.csv')
print(df.describe())

# histogram analizi
df.hist(figsize=(18, 12), bins=20, edgecolor='black')
plt.suptitle('veri dagilimi')

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Age', y='Cholesterol', hue='HeartDisease')

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')

# plt.show()


plt.figure(figsize=(6,6))
sns.countplot(x='HeartDisease',data=df)
plt.show()




# #model2

# print('model 2: Random Random Forest')
# rf_model=RandomForestClassifier(random_state=42)
# rf_model.fit(x_train_smote,y_train_smote)
# y_pred_rf=rf_model.predict(x_test_scaled)

