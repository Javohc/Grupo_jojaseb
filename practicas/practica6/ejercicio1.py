class instrumento:
    unidad_estandar = "SI"

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    @staticmethod
    def convertir_a_base(valor_mili):
        return valor_mili/1000
    
class Osciloscopio(instrumento):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

        self.v_div = 1.0 #no es necesario un def, ya que es un valor constante y no una variable

    def actualizar_v_div(self, nuevo_valor):
        self.v_div = nuevo_valor
        
    def imprimir_configuracion(self):
        print(f"Osciloscopio {self.marca} {self.modelo} | Voltaje/Div: {self.v_div} | Sistema: {self.unidad_estandar}")


mi_oscilo = Osciloscopio(marca="Tektronix",modelo="TBS1102B")

mi_oscilo.actualizar_v_div(0.5)
mi_oscilo.imprimir_configuracion()

v_mili = 500
v_base = instrumento.convertir_a_base(v_mili)
print(f"El valor {v_mili}[mV] equivale a {v_base}[V]")