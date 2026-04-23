def mover_servo(angulo):
    
    assert 0 <= angulo <= 180, "Error: el angulo esta fuera de rango"

    try:
        if not isinstance(angulo, (int)):
            raise TypeError("El angulo no es entero.")
    
    finally:
        print("Estado del motor: Standby")

mover_servo(45)
mover_servo(190)
mover_servo(67.8)