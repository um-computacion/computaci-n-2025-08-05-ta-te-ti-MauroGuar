from src.tablero import PosOcupadaException
from src.tateti import Tateti


def iniciar_cli():
    print("Bienvenidos al Tateti")

    juego = Tateti()

    while not juego.fin_juego():
        jugador_act = juego.obtener_jugador_act()
        print("Tablero: ")
        print(juego.tablero.contenedor)
        print(f"\nTurno de {jugador_act.obtener_nombre_jugador()} (Las '{jugador_act.obtener_ficha()}')")

        while True:
            try:
                fil = int(input("Ingrese fila: "))
                col = int(input("Ingrese columna: "))
            except ValueError:
                print("El valor debe ser un numero")
                continue

            tupla_verf = (0, 1, 2)
            if not (fil in tupla_verf and col in tupla_verf):
                print("Los valores deben estar entre 0 y 2")
                continue

            try:
                juego.ocupar_una_de_las_casillas(fil, col)
            except PosOcupadaException:
                print("La casilla ya está ocupada")
                continue
            break

    ganador = juego.obtener_ganador()
    if ganador is not None:
        print("\n\n---------->  JUEGO TERMINADO <----------")
        print(f"El ganador es: {ganador.obtener_nombre_jugador()}.")
    else:
        print("\n\n---------->  JUEGO TERMINADO <----------")
        print("Empate.")
