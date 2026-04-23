import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("calidad_aire.csv")

print(df.shape)
print(df.dtypes)
print(df.describe())

promedio_temp = df["temperatura"].mean()
print("El promedio de la temperatura es: ")
print(promedio_temp)

filtro = df[df["pm25"] > 35]
print(filtro)

df.to_csv("alerta_aire.csv", index=False)
