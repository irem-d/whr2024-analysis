
"""
Created on Wed Aug  2025

@author: İrem Demirtaş
"""




import pandas as pd

df = pd.read_csv("WHR2024.csv")

print(df.head())



print(df.info())


print(df.describe())


print(df.columns)






print(df.sort_values(by="Ladder score", ascending=False)[["Country name", "Ladder score"]].head())

print(df.sort_values(by="Ladder score")[["Country name", "Ladder score"]].head())



import matplotlib.pyplot as plt


top5 = df.sort_values(by="Ladder score", ascending=False).head()

plt.figure(figsize=(10,6))
plt.bar(top5["Country name"], top5["Ladder score"], color='green')
plt.title("En Mutlu 5 Ülke")
plt.ylabel("Ladder Score (Mutluluk Skoru)")
plt.xlabel("Ülke")
plt.ylim(0, 8)
plt.show()




factors = [
    'Explained by: Log GDP per capita',
    'Explained by: Social support',
    'Explained by: Healthy life expectancy',
    'Explained by: Freedom to make life choices',
    'Explained by: Generosity',
    'Explained by: Perceptions of corruption'
]

means = df[factors].mean().sort_values(ascending=False)

plt.figure(figsize=(12,6))
means.plot(kind='bar', color='skyblue')
plt.title('Mutluluğa En Çok Katkı Yapan Faktörler (Ortalama)')
plt.ylabel('Ortalama Değer')
plt.xticks(rotation=45, ha='right')
plt.show()




factors = [
    'Explained by: Log GDP per capita',
    'Explained by: Social support',
    'Explained by: Healthy life expectancy',
    'Explained by: Freedom to make life choices',
    'Explained by: Generosity',
    'Explained by: Perceptions of corruption'
]

means = df[factors].mean().sort_values(ascending=False)

plt.figure(figsize=(12,6))
means.plot(kind='bar', color='skyblue')
plt.title('Mutluluğa En Çok Katkı Yapan Faktörler (Ortalama)')
plt.ylabel('Ortalama Değer')
plt.xticks(rotation=45, ha='right')
plt.show()



import numpy as np


top5 = df.sort_values(by="Ladder score", ascending=False).head()


factors = [
    'Explained by: Log GDP per capita',
    'Explained by: Social support',
    'Explained by: Healthy life expectancy',
    'Explained by: Freedom to make life choices',
    'Explained by: Generosity',
    'Explained by: Perceptions of corruption'
]


data = top5[factors].values
labels = top5['Country name'].values

x = np.arange(len(factors))  
width = 0.15  

plt.figure(figsize=(14,7))

for i in range(len(labels)):
    plt.bar(x + i*width, data[i], width=width, label=labels[i])

plt.xticks(x + width*2.5, factors, rotation=45, ha='right')
plt.ylabel('Değer')
plt.title('En Mutlu 5 Ülkenin Mutluluğa Katkı Faktörleri')
plt.legend()
plt.tight_layout()
plt.show()


