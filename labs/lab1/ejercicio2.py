# EJERCICIO 2
vi = int(input("Ingrese valor de voltaje inicial Vi = "))
vq = int(input("Ingrese valor de voltaje minimo de operacion Vq = "))

contador = 0
while vq < vi:
    vi = vi * 0.95
    contador=contador+1

print(f"El banco logro entregar energia {contador} horas enteras antes de requerir recarga")