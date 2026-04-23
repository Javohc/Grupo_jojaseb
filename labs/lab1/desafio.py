## EJERCICIO 4
while True:
    x = int(input("Ingrese una lectura de temperatura (Grados celcius): "))

    if 20 < x < 45:
        print("Estado normal.")
    elif 45 < x <= 75:
        print("Advertencia: Encendiedo ventiladores auxiluares.")
    elif x > 75:
        print("¡Peligro critico! Apagando servidor de emergenicia.")
        break