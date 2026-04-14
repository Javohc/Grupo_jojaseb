def procesar_trama(trama):
    try:
        partes=trama.split(":")
        id_sensor=partes[0]

        valor=float(partes[1])
        print(f"ID: {id_sensor}, Valor: {valor}.")

    except ValueError:
        print("El dato ingresado no es un valor numerico.")

    except IndexError:
        print("La trama ingresada no contiene delimitador(:).")

    except Exception as e:
        print("Ocurrio un error no previsto.")

procesar_trama("250:45")
procesar_trama("250:hd")
