import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ventas_tienda.csv")

plt.figure()
plt.plot(df["Mes"], df["Laptops"], label="Laptops", color="green")
plt.plot(df["Mes"], df["Smartphones"], label="Smartphones", color="red")
plt.xlabel("Fecha")
plt.ylabel("Ventas")
plt.grid(True)
plt.legend()
plt.title("Ventas mensuales de lapotops y smartphones")
plt.show()
