import numpy as np

def cargar_experimentos():
    experimentos = {
        "exp1":  {"politica": "PPO",      "ambiente": "real",      "ruta": "simple",     "ISE": 434.99, "IAE": 135.93, "ITSE": 6932.79, "ITAE": 2601.61, "tiempo_s": None,   "pasos": None, "reward_medio": None},
        "exp2":  {"politica": "PPO-Mask", "ambiente": "real",      "ruta": "simple",     "ISE": 362.85, "IAE": 128.92, "ITSE": 5869.30, "ITAE": 2669.86, "tiempo_s": None,   "pasos": None, "reward_medio": None},
        "exp3":  {"politica": "PPO",      "ambiente": "simulated", "ruta": "simple",     "ISE": 73.35,  "IAE": 24.51,  "ITSE": 203.90,  "ITAE": 89.73,   "tiempo_s": None,   "pasos": None, "reward_medio": None},
        "exp4":  {"politica": "PPO-Mask", "ambiente": "simulated", "ruta": "simple",     "ISE": 73.79,  "IAE": 22.91,  "ITSE": 200.16,  "ITAE": 73.77,   "tiempo_s": None,   "pasos": None, "reward_medio": None},
        "exp5":  {"politica": "PPO",      "ambiente": "real",      "ruta": "square",     "ISE": None,   "IAE": None,   "ITSE": None,    "ITAE": None,    "tiempo_s": 112.48, "pasos": 594,  "reward_medio": 3.75},
        "exp6":  {"politica": "PPO-Mask", "ambiente": "real",      "ruta": "square",     "ISE": None,   "IAE": None,   "ITSE": None,    "ITAE": None,    "tiempo_s": 103.46, "pasos": 569,  "reward_medio": 4.13},
        "exp7":  {"politica": "PPO",      "ambiente": "simulated", "ruta": "square",     "ISE": None,   "IAE": None,   "ITSE": None,    "ITAE": None,    "tiempo_s": 27.89,  "pasos": 270,  "reward_medio": 7.12},
        "exp8":  {"politica": "PPO-Mask", "ambiente": "simulated", "ruta": "square",     "ISE": None,   "IAE": None,   "ITSE": None,    "ITAE": None,    "tiempo_s": 24.42,  "pasos": 235,  "reward_medio": 7.94},
        "exp9":  {"politica": "PPO",      "ambiente": "real",      "ruta": "triangular", "ISE": None,   "IAE": None,   "ITSE": None,    "ITAE": None,    "tiempo_s": 104.37, "pasos": 581,  "reward_medio": 3.92},
        "exp10": {"politica": "PPO-Mask", "ambiente": "real",      "ruta": "triangular", "ISE": None,   "IAE": None,   "ITSE": None,    "ITAE": None,    "tiempo_s": 116.71, "pasos": 638,  "reward_medio": 4.45},
        "exp11": {"politica": "PPO",      "ambiente": "simulated", "ruta": "triangular", "ISE": None,   "IAE": None,   "ITSE": None,    "ITAE": None,    "tiempo_s": 26.20,  "pasos": 254,  "reward_medio": 7.38},
        "exp12": {"politica": "PPO-Mask", "ambiente": "simulated", "ruta": "triangular", "ISE": None,   "IAE": None,   "ITSE": None,    "ITAE": None,    "tiempo_s": 22.75,  "pasos": 219,  "reward_medio": 8.25}
    }
    return experimentos

def generar_trayectoria_ideal(waypoints, puntos_por_segmento=100):

    x_ideal = []
    y_ideal = []

    for i in range(len(waypoints)-1): #Se resta 1 para evitar salirnos del limite de la lista de waypoints al buscar el punto siguiente
        punto_actual = waypoints[i]
        punto_siguiente = waypoints[i+1]

        x1, y1 = punto_actual[0], punto_actual[1]
        x2, y2 = punto_siguiente[0], punto_siguiente[1]
        
        x_segmento = np.linspace(x1, x2, puntos_por_segmento)
        y_segmento = np.linspace(y1, y2, puntos_por_segmento)
        
        x_ideal.extend(x_segmento)
        y_ideal.extend(y_segmento)

    return np.array(x_ideal), np.array(y_ideal)

def simular_lidar(n_sectores=36, d_min=0.5, d_max=30.0):
    angulos_deg = np.linspace(0, 360, n_sectores)
    
    distancias = np.random.uniform(d_min, d_max, n_sectores)

    # Al ser 4 elementos (9-5), se generan 4 nuevos valores aleatorios pequeños de entre 0.5 y 2.0 m
    distancias[5:9] = np.random.uniform(0.5, 2.0, 4)

    distancias_norm = (distancias - d_min) / (d_max - d_min)
    
    return angulos_deg, distancias, distancias_norm