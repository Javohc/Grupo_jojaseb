class Contenido:
    conteo_total = 0

    def __init__(self, titulo, año):

        Contenido.conteo_total += 1 #incrementa conteo_total cada que haya una instancia

        self.titulo = titulo
        self.año = año

    @classmethod
    def obtener_total(cls):
        return cls.conteo_total
    
class Pelicula(Contenido):
    def __init__(self, titulo, año, director, duracion):
        super().__init__(titulo, año)

        self.director = director
        self.duracion = duracion

    def mostrar_ficha(self):
        print(f"Titulo: {self.titulo} | Año: {self.año} | Director: {self.director} | Duracion: {self.duracion}")

pelicula1 = Pelicula("Up", 2009, "Pete Docter", 96)    
pelicula2 = Pelicula("Rapidos y Furiosos", 2001, "Rob Cohen", 106)    
pelicula3 = Pelicula("Baby Driver", 2017, "Edgar Wright", 113)  

pelicula1.mostrar_ficha()
pelicula2.mostrar_ficha()
pelicula3.mostrar_ficha()

print(f"El numero de peliculas en el catalogo es: {Contenido.obtener_total()}")