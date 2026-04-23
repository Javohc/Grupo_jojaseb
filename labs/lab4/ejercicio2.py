import pandas as pd

datos_juegos = {
    "Juego": ["Cyberpunk 2077", "Minecraft", "Hollow Knight", "FIFA 24"],
    "Precio_base": [40000, 15000, 7500, 45000],
    "Descuento_porcentaje": [50, 0, 20, 10]
}

df = pd.DataFrame(datos_juegos)

df["Precio_Final"] = df["Precio_base"] * (1-(df["Descuento_porcentaje"]/100))

filtro = df[df["Precio_Final"] < 20000]

print(filtro)