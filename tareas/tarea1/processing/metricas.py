import numpy as np

def calcular_IAE(errores, dt):
    iae = np.sum(np.abs(errores)) * dt
    return float(iae)

def calcular_ISE(errores, dt):
    ise = np.sum(errores**2) * dt
    return float(ise)

def calcular_ITAE(errores, dt):
    t = np.arange(len(errores)) * dt
    itae = np.sum(np.abs(errores) * t) * dt
    return float(itae)

def calcular_ITSE(errores, dt):
    t = np.arange(len(errores)) * dt
    itse = np.sum((errores**2) * t) * dt
    return float(itse)

def calcular_todas_las_metricas(errores, dt):
    iae = calcular_IAE(errores, dt)
    ise = calcular_ISE(errores, dt)
    itae = calcular_ITAE(errores, dt)
    itse = calcular_ITSE(errores, dt)

    resultados = {
        "IAE": round(iae, 2),
        "ISE": round(ise, 2),
        "ITAE": round(itae, 2),
        "ITSE": round(itse, 2)
    }

    return resultados

def calcular_mejora(valor_ppo, valor_mask):
    reduccion = ((valor_ppo-valor_mask)/valor_ppo)*100 # Funcion para verificar si ppo_mask mejora al ppo estantar (segun paper es 16.6% en ISE)
    
    return round(reduccion, 2)

