import numpy as pd
def calcular_impedancia():
    r = int(input("Ingrese valor de resistencia: "))
    x = int(input("Ingrese valor de reactancia: "))
   
    try:
        imp=pd.sqrt(r**2 + x**2)
        print(f"El valor de la impedancia es: {imp}")

    except ValueError:
        print("El valor ingresado no es un numero")
        return None
    
if __name__ == "__main__":
    calcular_impedancia()