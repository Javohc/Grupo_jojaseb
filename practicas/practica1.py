x = int(input("Ingrese un numero entero positivo: "))
suma = 0
a=0
b=1

for i in range(x+1):
    suma=a+b
    a=b
    b=suma
    print(f"la serie de Fibonacci del numero {x} es: {a}")