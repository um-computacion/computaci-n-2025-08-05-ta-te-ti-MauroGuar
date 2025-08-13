from src.jugador import Jugador
from src.tablero import Tablero


class Tateti:

    def __init__(self):
        self.jugador1 = Jugador("Jugador 1", 'X')
        self.jugador2 = Jugador("Jugador 2", 'O')
        self.jugador_act = self.jugador1
        self.ganador = None
        self.tablero = Tablero()

    def obtener_jugador_act(self):
        return self.jugador_act

    def obtener_ganador(self):
        return self.ganador

    def fin_juego(self) -> bool:
        return self.ganador is not None or self.verf_empate()

    def ocupar_una_de_las_casillas(self, fil, col):
        self.tablero.poner_la_ficha(fil, col, self.jugador_act.obtener_ficha())

        verificacion_ganar = self.verf_ganar(fil, col)
        if verificacion_ganar:
            self.ganador = self.jugador_act
            return

        if self.jugador_act == self.jugador1:
            self.jugador_act = self.jugador2
        else:
            self.jugador_act = self.jugador1

    def verf_ganar(self, fil, col) -> bool:
        ficha_act = self.jugador_act.obtener_ficha()
        cont = self.tablero.contenedor
        if all(cont[fil][i] == ficha_act for i in range(3)):
            return True
        if all(cont[i][col] == ficha_act for i in range(3)):
            return True
        if fil == col and all(cont[i][i] == ficha_act for i in range(3)):
            return True
        if fil + col == 2 and all(cont[i][2 - i] == ficha_act for i in range(3)):
            return True
        return False

    def verf_empate(self):
        return all(self.tablero.contenedor[i][j] != "" for i in range(3) for j in range(3))
