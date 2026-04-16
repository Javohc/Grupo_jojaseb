import matplotlib.pyplot as plt
import os

def plot_metricas(diccionario_experimentos, ambiente, ruta):
    datos_ppo = {} # Con {} y no con [], ya que al querer solo un valor del diccionario es mas facil su implementacion
    datos_mask = {} # Y no es necesario primero indicar la lista y luego el diccionario. No dara erorr, ya que el main lo llama mas de una vez para generar cada grafico

    for experimentos, datos in diccionario_experimentos.items():
        if datos["ambiente"] == ambiente and datos["ruta"] == ruta:
            if datos["politica"] == "PPO":
                datos_ppo = datos
            elif datos["politica"] == "PPO-Mask":
                datos_mask = datos

    # Verificamos que encontramos los datos para no generar gráficos vacíos
    if not datos_ppo or not datos_mask:
        print(f"No se encontraron datos para ambiente='{ambiente}' y ruta='{ruta}'")
        return

    plt.figure()
    metricas = ["ISE", "IAE", "ITSE", "ITAE"]

    # Grafico ISE
    plt.subplot(1, 4, 1)
    v_ppo = datos_ppo["ISE"] if datos_ppo['ISE'] is not None else 0
    v_mask = datos_mask["ISE"] if datos_mask['ISE'] is not None else 0
    
    plt.bar(["PPO", "PPO-Mask"], [v_ppo, v_mask], color="green")
    plt.title("ISE")
    plt.ylabel("Valor del índice")

    # Grafico IAE
    plt.subplot(1, 4, 2)
    v_ppo = datos_ppo["IAE"] if datos_ppo['IAE'] is not None else 0
    v_mask = datos_mask["IAE"] if datos_mask['IAE'] is not None else 0
    
    plt.bar(["PPO", "PPO-Mask"], [v_ppo, v_mask], color="red")
    plt.title("IAE")

    # Grafico ITSE
    plt.subplot(1, 4, 3)
    v_ppo = datos_ppo["ITSE"] if datos_ppo['ITSE'] is not None else 0
    v_mask = datos_mask["ITSE"] if datos_mask['ITSE'] is not None else 0
    
    plt.bar(["PPO", "PPO-Mask"], [v_ppo, v_mask], color="blue")
    plt.title("ITSE")

    # Grafico ITAE
    plt.subplot(1, 4, 4)
    v_ppo = datos_ppo["ITAE"] if datos_ppo['ITAE'] is not None else 0
    v_mask = datos_mask["ITAE"] if datos_mask['ITAE'] is not None else 0
    
    plt.bar(["PPO", "PPO-Mask"], [v_ppo, v_mask], color="black")
    plt.title("ITAE")

    carpeta_destino = "resultados_graficos"
    
    # exist_ok=True crea la carpeta si no existe, y si ya existe, no hace nada 
    os.makedirs(carpeta_destino, exist_ok=True)
    
    ruta_guardado = os.path.join(carpeta_destino, f"metricas_{ambiente}_{ruta}.png")
    plt.savefig(ruta_guardado, dpi=300)
    plt.close()

def plot_lidar(angulos, distancias, distancias_norm):
    plt.figure()

    plt.subplot(1, 2, 1)
    plt.scatter(angulos, distancias, color="red")
    plt.title("Distancias de los obstaculos")
    plt.xlabel("Ángulo (0-360°)")
    plt.ylabel("Distancia (m)")
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(angulos, distancias_norm, color="green")
    plt.title("Distancias normalizadas")
    plt.xlabel("Ángulo (0-360°)")
    plt.ylabel("Valor (0.0 a 1.0)")
    plt.grid(True)
    
    carpeta_destino = "resultados_graficos"
    os.makedirs(carpeta_destino, exist_ok=True)
    
    ruta_guardado = os.path.join(carpeta_destino, "mapa_lidar.png")
    plt.savefig(ruta_guardado, dpi=300)
    plt.close()

def plot_trayectorias(x_ppo, y_ppo, x_mask, y_mask, waypoints, nombre):
    plt.figure()

    plt.plot(x_ppo, y_ppo, label="Trayectoria PPO", color="blue")
    plt.plot(x_mask, y_mask, label="Trayectoria PPO-Mask", color="green", linestyle='--')

    x_wp = [punto[0] for punto in waypoints] # Como los waypoints son de la forma [x,y] hay que separarlos para poder aplicar scatter
    y_wp = [punto[1] for punto in waypoints]
    
    plt.scatter(x_wp, y_wp, color="black", marker="s", label="Waypoints")

    plt.axis("equal")

    plt.title(f"Comparación de Navegación: {nombre}")
    plt.xlabel("Posición X (m)")
    plt.ylabel("Posición Y (m)")
    plt.legend()
    plt.grid(True)
    
    carpeta_destino = "resultados_graficos"
    os.makedirs(carpeta_destino, exist_ok=True)
    
    ruta_guardado = os.path.join(carpeta_destino, f"trayectorias_{nombre}.png")
    plt.savefig(ruta_guardado, dpi=300)
    plt.close()