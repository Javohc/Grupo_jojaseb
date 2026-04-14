def promedio_sensor():
    # Base de datos simulada en memoria
    sensores = {
        "temp": [22.5, 23.1, 22.8], 
        "presion": [1013, 1015], 
        "humedad": []
    }
    
    nombre_sensor = input("Ingrese nombre del sensor (temp, presion, humedad): ")
    
    try:
        lecturas = sensores[nombre_sensor]
        
        promedio = sum(lecturas) / len(lecturas)
        print(f"El promedio de las lecturas del sensor '{nombre_sensor}' es: {promedio}")
        
    except KeyError:
        print(f"Error: El sensor '{nombre_sensor}' no se encuentra registrado.")
        
    except ZeroDivisionError:
        print(f"Advertencia: El sensor '{nombre_sensor}' no tiene lecturas registradas.")
        
    finally:
        print("Consulta de sensor finalizada.\n")

if __name__ == "__main__":
    promedio_sensor()