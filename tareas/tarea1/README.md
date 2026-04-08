# Tarea 1: Sistema de Análisis Robótico

## Descripción
Este directorio contiene la estructura principal para el sistema de análisis robótico. El proyecto está modularizado en distintos paquetes para separar la lógica de ejecución, análisis matemático y visualización.

## Estructura del Proyecto
La carpeta está organizada de la siguiente manera:

```text
tarea1/
├── main.py            # Script principal de ejecución
├── data/              # Datos de paper y generacion de señales
│   └── __init__.py         
├── processing/        # Calculos de ecuaciones
│   └── __init__.py         
└── visualization/     # Generacion de figuras para visualizacion de datos
    └── __init__.py
```

## Notas de desarrollo
El uso de los archivos "__init__.py" en cada paquete sirve para convertir carpetas en paquetes de python, le indica que tienen módulos de código. Ademas permite importar funciones hacia el script main.
Y para funciones de github sirve para subir la estructura de directorios al repositorio directamente al tener un archivo dentro.
