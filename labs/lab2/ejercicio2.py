#---Datos para el Ejercicio 2 (Listas)--
coords_x = [2, 8, 8, 2]
coords_y = [1, 1, 5, 5]

def evaluar_zona_poligono(x, y):
    # Bounding box
    ancho = max(x) - min(x)
    alto = max(y) - min(y)

    area = ancho*alto

    x_centro = sum(x) / len(x)
    y_centro = sum(y) / len(y)

    centro = (x_centro, y_centro)

    return area, centro

area, centro = evaluar_zona_poligono(coords_x, coords_y)

print("Area de la caja delimitada")
print("Area: ", area)
print("------------------------------------------")
print("Centro de la caja a analizar")
print("Centro: ", centro)