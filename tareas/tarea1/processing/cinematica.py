import numpy as np

def calcular_movimiento(x, y, theta, v, omega, dt=0.1):
    v_lim = np.clip(v, -0.8, 0.8) # Se coloca -0.8 y no 0, para que el robot pueda frenar
    omega_lim = np.clip(omega, -0.6, 0.6) # Lo mismo para que pueda girar a ambos lados
    
    x_nuevo = x + v_lim * np.cos(theta) * dt
    y_nuevo = y + v_lim * np.sin(theta) * dt
    
    theta_nuevo = theta + omega_lim * dt
    
    return (x_nuevo, y_nuevo, theta_nuevo)


def distancia_al_objetivo(x, y, x_meta, y_meta):
    
    distancia = np.sqrt((x_meta-x)**2 + (y_meta-y)**2)
    
    return distancia


def calcular_error_seguimiento(x_real, y_real, x_ideal, y_ideal):

    min_len = min(len(x_real), len(x_ideal)) # Tamaño minimo entre la ruta real e ideal. como los vectores x e y tendran el mismo tamaño, solo se busca el valor minimo una vez para cuestiones de eficiencia de codigo
    
    # Recorta todos los arreglos para que tengan exactamente el mismo tamaño
    x_r = x_real[:min_len]
    y_r = y_real[:min_len]
    x_i = x_ideal[:min_len]
    y_i = y_ideal[:min_len]

    
    errores = np.sqrt((x_r-x_i)**2 + (y_r-y_i)**2)
    
    return errores