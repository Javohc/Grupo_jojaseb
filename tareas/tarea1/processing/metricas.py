import numpy as np

def calcular_IAE(errores, dt):
    # IAE (Integral Absolute Error): sumatoria del valor absoluto del error por dt
    iae = np.sum(np.abs(errores)) * dt
    return float(iae)

def calcular_ISE(errores, dt):
    # ISE (Integral Square Error): sumatoria del error al cuadrado por dt
    ise = np.sum(errores**2) * dt
    return float(ise)

def calcular_ITAE(errores, dt):
    # Generamos el vector de tiempo
    t = np.arange(len(errores)) * dt
    # ITAE: sumatoria del valor absoluto del error por el tiempo por dt
    itae = np.sum(np.abs(errores) * t) * dt
    return float(itae)

def calcular_ITSE(errores, dt):
    # Generamos el vector de tiempo
    t = np.arange(len(errores)) * dt
    # ITSE: sumatoria del error al cuadrado por el tiempo por dt
    itse = np.sum((errores**2) * t) * dt
    return float(itse)