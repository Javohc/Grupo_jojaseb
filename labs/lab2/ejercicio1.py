#---Datos para el Ejercicio 1 (Diccionarios)---
red_esp8266 = {
    "Nodo_Tanque": {"ip": "192.168.1.10", "estado": "activo", "salida_dac": 3000},
    "Nodo_Motor": {"ip": "192.168.1.11", "estado": "falla", "salida_dac": 0},
    "Nodo_Valvula": {"ip": "192.168.1.12", "estado": "inactivo", "salida_dac": 150},
    "Nodo_Caldera": {"ip": "192.168.1.13", "estado": "activo", "salida_dac": 4000}
}

#---Datos para el Ejercicio 2 (Listas)--
coords_x = [2, 8, 8, 2]
coords_y = [1, 1, 5, 5]

#---Datos para el Ejercicio 3 (Tuplas y Diccionarios)--
# Puedes desempaquetar esta tupla en *args
angulos_prueba = (45, 90,-30, 15)

# Puedes desempaquetar este diccionario en **kwargs
configuracion_robot = {
    "velocidad": 50,
    "torque_max": 120,
    "herramienta": "pinza"
}

def auditar_red(nodos):
    nro_nodos=len(red_esp8266)

    #lista estados
    falla = []
    inactivos = []
    activos = []

    for nombre, datos in nodos.items():
        estado = datos["estado"]
        ip = datos["ip"]
        salida_dac = datos["salida_dac"]

   
        if estado == "activo":
            activos.append(salida_dac)
   
        elif estado == "falla":
            falla.append(ip)

        else:
            inactivos.append(ip)

    promedio = sum(activos)/len(activos)

    return nro_nodos, activos, falla, inactivos, promedio

nro_nodos, activos, falla, inactivos, promedio = auditar_red(red_esp8266)

print("Cantidad total de nodos registrados")
print("Cantidad: ", nro_nodos)
print("------------------------------------------")
print("Lista IP de los nodos en falla")
print("IPs: ", falla)
print("------------------------------------------")
print("Lista IP de los nodos inactivos")
print("IPs: ", inactivos)
print("------------------------------------------")
print("Promedio de salida_dac de nodos activos")
print("Promedio: ", promedio)

    
