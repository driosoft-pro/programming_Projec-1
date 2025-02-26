import random  # Importa la librería random para generar números aleatorios
import os  # Importa el módulo os para limpiar la pantalla

# Función para limpiar la pantalla de la consola.
def limpiar_pantalla():
    if os.name == "nt":  # Verifica si el sistema operativo es Windows
        os.system("cls")  # Ejecuta el comando "cls" para limpiar la pantalla en Windows
    else:
        os.system("clear")  # Ejecuta el comando "clear" para limpiar la pantalla en sistemas tipo Unix

# Función para mostrar el título del juego.
def mostrar_titulo():
    print("=== === === === === === ESTAMOS JUGANDO BATALLA NAVAL === === === === === ===")  # Imprime el título del juego y un salto de línea al final

# ======================= BATALLA NAVAL =======================
# Sección principal que define las funciones y la lógica del juego Batalla Naval.

def mostrar_reglas_batalla_naval():
    # Muestra las reglas del juego en pantalla.
    print("\n======================== REGLAS DE BATALLA NAVAL ========================")
    print("- Tablero de 5x5, cada jugador tiene 3 barcos.")
    print("- La máquina coloca sus barcos aleatoriamente.")
    print("- Tú debes ingresar las coordenadas de tus barcos.")
    print("- En cada turno, atacas una posición e intentas hundir los barcos enemigos.")
    print("- Gana quien hunda primero los 3 barcos del oponente.")
    print("===========================================================================\n")

def crear_tablero():
    # Crea y retorna un tablero vacío de 5x5. Cada celda es un espacio en blanco.
    return [[" "] * 5 for _ in range(5)]

def imprimir_tablero(tablero):
    # Imprime el tablero con encabezados de columnas y el índice de cada fila.
    print("  0 1 2 3 4")  # Encabezado de columnas
    for i, fila in enumerate(tablero):
        print(i, " ".join(fila))  # Imprime el índice de la fila seguido de las celdas (unidas por espacios)

def colocar_barcos(tablero, cantidad):
    # Coloca de manera aleatoria "cantidad" barcos (representados por "B") en el tablero.
    barcos_colocados = 0
    while barcos_colocados < cantidad:
        # Genera aleatoriamente las coordenadas (fila y columna) entre 0 y 4.
        fila, columna = random.randint(0, 4), random.randint(0, 4)
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = "B"  # Coloca un barco en la posición seleccionada
            barcos_colocados += 1  # Incrementa el contador al colocar un barco

def colocar_barcos_jugador(tablero):
    # Permite al jugador colocar 3 barcos en el tablero ingresando sus coordenadas.
    barcos_colocados = 0
    while barcos_colocados < 3:
        try:
            # Solicita la fila y la columna para colocar el barco actual.
            fila = int(input(f"Ingresa la fila para el barco {barcos_colocados + 1} (0-4): "))
            columna = int(input(f"Ingresa la columna para el barco {barcos_colocados + 1} (0-4): "))
            # Verifica que las coordenadas sean válidas (en rango y que la celda esté libre).
            if 0 <= fila <= 4 and 0 <= columna <= 4 and tablero[fila][columna] == " ":
                tablero[fila][columna] = "B"  # Coloca el barco del jugador
                barcos_colocados += 1  # Incrementa el contador
            else:
                print("Posición inválida o ya ocupada, intenta de nuevo.")
        except ValueError:
            print("Entrada inválida, ingresa números entre 0 y 4.")
        except KeyboardInterrupt:
            print("\nHas abandonado la partida. ¡Perdiste!")
            exit()  # Sale del programa si el usuario cancela

def contar_intentos(intentos):
    # Imprime el número de intentos realizados por el jugador.
    print(f"\n🃏 Número de intentos usados: {intentos}\n")

def jugar_batalla_naval():
    # Función principal que gestiona el flujo del juego.
    mostrar_reglas_batalla_naval()  # Muestra las reglas del juego al inicio.
    tablero_jugador = crear_tablero()   # Crea el tablero del jugador.
    tablero_maquina = crear_tablero()   # Crea el tablero de la máquina.
    tablero_ataques = crear_tablero()    # Crea un tablero para que el jugador vea los resultados de sus ataques.
    
    print("\nColoca tus barcos:")
    colocar_barcos_jugador(tablero_jugador)  # Permite que el jugador coloque sus 3 barcos.
    colocar_barcos(tablero_maquina, 3)         # Coloca aleatoriamente 3 barcos en el tablero de la máquina.
    
    # Inicializa los contadores de barcos restantes para cada participante.
    barcos_jugador = 3  
    barcos_maquina = 3  
    intentos = 0  # Contador de intentos realizados por el jugador
    
    # Bucle principal del juego que se ejecuta mientras ambos tengan barcos.
    while barcos_jugador > 0 and barcos_maquina > 0:
        limpiar_pantalla()  # Limpia la pantalla antes de cada turno
        mostrar_titulo()  # Muestra el título del juego
        mostrar_reglas_batalla_naval()  # Muestra las reglas del juego al inicio.
        imprimir_tablero(tablero_ataques)  # Muestra el tablero con los ataques realizados hasta el momento.
        contar_intentos(intentos)  # Muestra el número de intentos realizados por el jugador
        
        # Turno del jugador
        try:
            # Solicita al jugador las coordenadas de ataque.
            fila = int(input("Ingresa la fila para atacar (0-4): "))
            columna = int(input("Ingresa la columna para atacar (0-4): "))
            if 0 <= fila <= 4 and 0 <= columna <= 4:
                if tablero_maquina[fila][columna] == "B":
                    print("¡Impacto! Hundiste un barco enemigo.")
                    tablero_maquina[fila][columna] = "X"  # Marca en el tablero de la máquina que el barco fue hundido.
                    tablero_ataques[fila][columna] = "X"   # Indica un ataque exitoso en el tablero de ataques.
                    barcos_maquina -= 1  # Reduce la cantidad de barcos de la máquina.
                else:
                    print("Agua. No impactaste ningún barco.")
                    tablero_ataques[fila][columna] = "O"  # Marca en el tablero de ataques un fallo.
                intentos += 1  # Incrementa el contador de intentos
            else:
                print("Coordenadas fuera de rango.")
        except ValueError:
            print("Entrada inválida, ingresa números entre 0 y 4.")
        except KeyboardInterrupt:
            print("\nHas abandonado la partida. ¡Perdiste!")
            exit()  # Sale del programa si el usuario cancela
        
        # Turno de la máquina (se ejecuta siempre y cuando queden barcos en la máquina)
        if barcos_maquina > 0:
            # La máquina selecciona aleatoriamente las coordenadas para atacar.
            fila, columna = random.randint(0, 4), random.randint(0, 4)
            if tablero_jugador[fila][columna] == "B":
                print(f"La máquina atacó ({fila}, {columna}) y hundió uno de tus barcos.")
                tablero_jugador[fila][columna] = "X"  # Marca el barco del jugador como hundido.
                barcos_jugador -= 1  # Reduce el contador de barcos del jugador.
            else:
                print(f"La máquina atacó ({fila}, {columna}) pero falló.")
    
    # Se determina el resultado final del juego.
    limpiar_pantalla()
    mostrar_titulo()
    if barcos_jugador == 0:
        print("\nLa máquina ha ganado la Batalla Naval. ¡Mejor suerte la próxima vez!")
    else:
        print("\n¡Felicidades! Has ganado la Batalla Naval.")

# Programa principal: verifica si el script es ejecutado directamente
if __name__ == "__main__":
    try:
        jugar_batalla_naval()  # Inicia la ejecución del juego.
    except KeyboardInterrupt:
        print("\nHas abandonado la partida. ¡Perdiste!")  # Captura el cierre abrupto del juego