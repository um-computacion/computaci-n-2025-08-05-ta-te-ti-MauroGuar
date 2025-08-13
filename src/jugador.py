class Jugador:
    def __init__(self, nombre_jugador, ficha):
        self.nombre_jugador = nombre_jugador
        self.ficha = ficha

    def obtener_nombre_jugador(self):
        return self.nombre_jugador

    def obtener_ficha(self):
        return self.ficha
