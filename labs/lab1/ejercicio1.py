# EJERCICIO 1
v = int(input("Ingrese valor de voltaje V = "))
i = int(input("Ingrese valor de voltaje I = "))

R = v / i
P = v * i
print(f"El valor de la resistencia es: {R}")
print(f"El valor de la potencia es: {P}")

if P > 1000:
    print("¡Peligro! lta disipacion de potencia detectada")
else:
    print("Operacion en rangos seguros")