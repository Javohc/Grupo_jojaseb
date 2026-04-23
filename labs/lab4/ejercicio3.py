import pandas as pd

df = pd.read_csv("notas_alumnos.csv")

df_clean = df.dropna()

df_clean["Promedio"] = (df_clean["Parcial_1"] + df_clean["Parcial_2"]) / 2

print(df_clean)

