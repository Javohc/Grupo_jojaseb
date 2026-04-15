class PistaAudio:
    plataforma = "Spotify"

    def __init__(self, titulo, duracion):

        self.titulo = titulo
        self.duracion = duracion

    @staticmethod
    def formatear_tiempo(segundos):
        minutos = segundos // 60
        seg_restantes = segundos % 60
        return f"{minutos}:{seg_restantes}"
    
class Cancion(PistaAudio):
    def __init__(self, titulo, duracion, artista, genero):
        super().__init__(titulo, duracion)

        self.artista = artista
        self.genero = genero

    def reproducir(self):
        print(f"¡Buen gusto!, reproduciendo {self.titulo} en {self.plataforma}")

mi_song = Cancion("2.0", 169, "BTS", "K-POP")

mi_song.reproducir()

tiempo = PistaAudio.formatear_tiempo(mi_song.duracion)
print(f"Duracion de la cancion: {tiempo}")
