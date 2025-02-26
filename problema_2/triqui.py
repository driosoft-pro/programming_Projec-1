import random
import os  # Importa el módulo os para limpiar la pantalla.

# Función para limpiar la pantalla de la consola.
def limpiar_pantalla():
    # Verifica el sistema operativo y ejecuta el comando correspondiente.
    if os.name == "nt":  # Para Windows.
        os.system("cls")
    else:  # Para macOS y Linux.
        os.system("clear")

# Función para mostrar el título del juego.
def mostrar_titulo():
    print("=== ESTAMOS JUGANDO TRIQUI ===\n")

# ======================= TRIQUI (Tic-Tac-Toe) =======================
# Funciones y lógica del juego Tic-Tac-Toe.

def mostrar_reglas_triqui():
    # Muestra las reglas del juego en pantalla.
    print("\n===== REGLAS DE TRIQUI =====")
    print("- Juego en un tablero de 3x3.")
    print("- Dos jugadores: Tú (X) vs Máquina (O).")
    print("- Gana quien complete una fila, columna o diagonal con su símbolo.")
    print("- Si el tablero se llena y no hay ganador, es un empate.")
    print("===================================\n")

def crear_tablero_triqui():
    # Crea y retorna un tablero vacío de 3x3, utilizando espacios para celdas vacías.
    return [[" "] * 3 for _ in range(3)]

def imprimir_tablero_triqui(tablero):
    # Imprime el estado actual del tablero con índices de filas y columnas.
    print("    0   1   2")  # Encabezado de columnas.
    print("  -------------")
    for i, fila in enumerate(tablero):
        print(f"{i} | {' | '.join(fila)} |")  # Muestra el índice de la fila y las celdas.
        print("  -------------")

def verificar_ganador(tablero, jugador):
    # Verifica si el jugador (X o O) ha ganado el juego.
    # Revisa todas las filas.
    for fila in tablero:
        if all(celda == jugador for celda in fila):
            return True
    # Revisa todas las columnas.
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True
    # Revisa la diagonal principal y la secundaria.
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)):
        return True
    return False  # No se encontró una condición ganadora.

def obtener_entrada_usuario():
    # Solicita al jugador la fila y la columna, validando la entrada.
    while True:
        try:
            fila = int(input("Ingresa la fila (0-2): "))
            columna = int(input("Ingresa la columna (0-2): "))
            if 0 <= fila <= 2 and 0 <= columna <= 2:
                return fila, columna
            else:
                print("Error: Las filas y columnas deben estar entre 0 y 2. Intenta de nuevo.")
        except ValueError:
            print("Error: Entrada inválida. Debes ingresar números enteros. Intenta de nuevo.")
        except KeyboardInterrupt:
            print("\nHas abandonado el juego.")
            exit()  # Sale del programa.

def jugar_triqui():
    # Función principal que ejecuta el juego.
    mostrar_reglas_triqui()  # Muestra las reglas al jugador.
    tablero = crear_tablero_triqui()  # Inicializa el tablero 3x3 vacío.
    turno_jugador = random.choice([True, False])  # Determina aleatoriamente quién comienza (True para jugador, False para máquina).
    
    # Bucle principal: máximo 9 jugadas (número de celdas en el tablero).
    for _ in range(9):
        limpiar_pantalla()  # Limpia la pantalla antes de imprimir el tablero.
        mostrar_titulo()  # Muestra el título del juego.
        mostrar_reglas_triqui()  # Muestra las reglas al jugador.
        imprimir_tablero_triqui(tablero)  # Muestra el estado del tablero en cada turno.
        if turno_jugador:
            # Si es el turno del jugador:
            while True:
                try:
                    fila, columna = obtener_entrada_usuario()  # Obtiene la entrada del usuario.
                    if tablero[fila][columna] == " ":
                        tablero[fila][columna] = "❌"  # Coloca la marca del jugador.
                        if verificar_ganador(tablero, "❌"):
                            limpiar_pantalla()
                            mostrar_titulo()
                            imprimir_tablero_triqui(tablero)
                            print("\n¡Felicidades, ganaste!")
                            return  # Termina el juego si el jugador gana.
                        turno_jugador = False  # Cambia turno a la máquina.
                        break
                    else:
                        print("Error: La posición ya está ocupada. Intenta de nuevo.")
                except KeyboardInterrupt:
                    print("\nHas abandonado el juego.")
                    exit()  # Sale del programa.
                except Exception as e:
                    print(f"Error inesperado: {e}. Intenta de nuevo.")
        else:
            # Turno de la máquina:
            fila, columna = random.randint(0, 2), random.randint(0, 2)
            # Asegura que se elija una posición vacía.
            while tablero[fila][columna] != " ":
                fila, columna = random.randint(0, 2), random.randint(0, 2)
            tablero[fila][columna] = "⭕"  # Coloca la marca de la máquina.
            if verificar_ganador(tablero, "⭕"):
                limpiar_pantalla()
                mostrar_titulo()
                imprimir_tablero_triqui(tablero)
                print("\nLa máquina ha ganado. ¡Inténtalo de nuevo!")
                return  # Termina el juego si la máquina gana.
            turno_jugador = True  # Cambia turno al jugador.
    # Si se completan todas las jugadas sin ganador, se declara empate.
    limpiar_pantalla()
    mostrar_titulo()
    imprimir_tablero_triqui(tablero)
    print("\nEs un empate.")

# Programa principal: se ejecuta cuando el script se invoca directamente.
if __name__ == "__main__":
    try:
        jugar_triqui()  # Inicia la ejecución del juego.
    except KeyboardInterrupt:
        print("\nHas abandonado el juego.")