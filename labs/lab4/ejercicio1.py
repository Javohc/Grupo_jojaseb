import pandas as pd

data = {
    "Cancion": ["Deja Vu", "FaSHioN", "1-800-hot-n-fun", "FANCY"],
    "Artista": ["TXT", "Cortis", "LE SSERAFIM", "TWICE"],
    "Duracion_seg": [150.6, 152.3, 151.8, 199,8]
}

df = pd.DataFrame(data)
print("Las dimensiones de Data es:")
print(df.shape)

print(df.dtypes)