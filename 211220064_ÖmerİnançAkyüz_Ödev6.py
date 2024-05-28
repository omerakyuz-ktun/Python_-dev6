import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x_koordinatlar = np.random.randint(0, 1001, 1000)
y_koordinatlar = np.random.randint(0, 1001, 1000)

df = pd.DataFrame({"X": x_koordinatlar, "Y": y_koordinatlar})

df.to_excel("koordinatlar.xlsx")

df = pd.read_excel("koordinatlar.xlsx")
x = df["X"].values
y = df["Y"].values

plt.figure(figsize=(8, 8))  

izgara_boyutu = 200

for i in range(0, 1001, izgara_boyutu):
    plt.axvline(i, color='gray', linewidth=0.5)
    plt.axhline(i, color='gray', linewidth=0.5)

renkler = np.random.rand(len(x), 3)

for i in range(len(x)):
    izgara_x = x[i] // izgara_boyutu
    izgara_y = y[i] // izgara_boyutu
    plt.scatter(x[i], y[i], color=renkler[izgara_x * (1000 // izgara_boyutu) + izgara_y], s=10)

plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.grid(True)
plt.show()