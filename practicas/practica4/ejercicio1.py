import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sensor_datos.csv")
df_clean = df.dropna()

print(df_clean.head())

df_clean["potencia_W"] = df_clean["voltaje"] * df_clean["corriente"]

df_clean["alerta_humedad"] = df_clean["humedad"] > 70

plt.figure()
plt.plot(df_clean["fecha"], df_clean["temperatura"], label="Temperatura")
plt.plot(df_clean["fecha"], df_clean["potencia_W"], label="Potencia")
plt.xticks(rotation=45)
plt.xlabel("Fecha")
plt.ylabel("Magnitud")
plt.grid(True)
plt.legend()
plt.title("Grafica de temperatura y voltaje respecto a la fecha")
plt.show()

