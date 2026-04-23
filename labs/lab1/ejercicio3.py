# EJERCICIO 3
x = 0
while x != 4:
    print("1. Convertir miliamperios (mA) a amperios (A).")
    print("2. Convertir microfaradios (uF) a faradios (F).")
    print("3. Convetir kiloohmios (kohm) a ohmios (ohm).")
    print("4. Salir.")

    x = int(input("Ingrese numero de pestaña que desea ingresar: "))

    if x == 1:
        mili=int(input("Ingrese valor en miliamperios: "))
        a = mili/1000
        print(f"El valor el amperios es: {a}[A].")
    elif x == 2:
        micro = int(input("Ingrese valor en microfaradios: "))
        b = micro/1000000
        print(f"El valor en faradios es: {b} [F].")
    elif x == 3:
        kilo = int(input("Ingrese valor en kiloohmios: "))
        c = kilo*1000
        print(f"El valor en ohmios es: {c} [ohm].")
    elif x == 4:
        print("Sesión cerrada")
    else:
        print("ERROR: Ingresar valor valido.")