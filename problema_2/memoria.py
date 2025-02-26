import random  # Importa el módulo random para operaciones aleatorias
import os  # Importa el módulo os para limpiar la pantalla

# ======================= JUEGO DE MEMORIA =======================

def mostrar_titulo():
    # Muestra el título del juego en la consola
    print("\n======================")  # Imprime línea separadora superior
    print("   🎴 JUEGO DE MEMORIA 🎴")  # Imprime el título embellecido
    print("======================\n")  # Imprime línea separadora inferior y salto de línea

def mostrar_reglas():
    # Muestra las reglas del juego en la consola
    print("\n===== REGLAS DEL JUEGO DE MEMORIA =====")  # Imprime el encabezado de las reglas
    print("- Tablero de 6x5 con 15 pares de figuras ocultas.")  # Explica el tamaño del tablero y la cantidad de pares
    print("- Encuentra los pares destapando dos cartas por turno.")  # Indica la mecánica de elegir cartas
    print("- Si aciertas, el par queda visible y ganas un punto.")  # Explica la recompensa de acertar un par
    print("- Si fallas, las cartas se vuelven a tapar.")  # Indica que las cartas se ocultan nuevamente en caso de fallo
    print("- Gana quien descubra más pares.")  # Establece la condición de victoria
    print("===================================\n")  # Imprime línea inferior de separación

def generar_tablero():
    # Genera un tablero con las figuras en posiciones aleatorias
    figuras = ["🍎", "🍌", "🍉", "🍓", "🍒", "🥝", "🍇", "🍍", "🥕", "🌽", "🥑", "🥥", "🍄", "🥒", "🌶"]  # Lista de 15 figuras
    figuras *= 2  # Duplica la lista para generar pares de cada figura (15 pares en total)
    random.shuffle(figuras)  # Mezcla aleatoriamente la lista de figuras
    return [figuras[i * 5:(i + 1) * 5] for i in range(6)]  # Crea y devuelve una matriz de 6 filas y 5 columnas

def generar_tablero_oculto():
    # Genera un tablero oculto donde todas las cartas aparecen como "❓"
    return [["❓"] * 5 for _ in range(6)]  # Retorna una lista de 6 listas, cada una con 5 "❓"

def imprimir_tablero(tablero):
    # Imprime el tablero en la consola de forma formateada
    print("  0 1 2 3 4")  # Imprime los índices de las columnas
    for i, fila in enumerate(tablero):  # Itera sobre cada fila junto con su índice
        print(i, " ".join(fila))  # Imprime el índice de la fila y los elementos de la misma separados por espacios

def contar_manos(intentos):
    # Imprime el número de intentos utilizados hasta el momento
    print(f"\n🃏 Número de intentos usados: {intentos}\n")  # Muestra el contador de intentos en consola

def jugar_memoria():
    # Función principal que ejecuta la lógica completa del juego de memoria

    mostrar_titulo()  # Llama a la función que muestra el título del juego
    mostrar_reglas()  # Llama a la función que muestra las reglas del juego
    
    tablero = generar_tablero()  # Crea el tablero con las figuras ya mezcladas
    tablero_oculto = generar_tablero_oculto()  # Crea un tablero de visualización con todas las cartas ocultas
    puntos_jugador, puntos_maquina, intentos = 0, 0, 0  # Inicializa puntajes para el jugador, la máquina y la cantidad de intentos
    pares_encontrados = 0  # Inicializa el contador de pares encontrados
    
    while pares_encontrados < 15:  # Bucle que continúa hasta encontrar los 15 pares
        imprimir_tablero(tablero_oculto)  # Muestra el estado actual del tablero oculto
        
        try:
            print("\nTu turno: Elige dos cartas para destapar.")  # Indica al jugador que seleccione dos cartas
            # Solicita al jugador la fila y columna de la primera carta a destapar
            fila1 = int(input("Ingresa la fila de la primera carta (0-5): "))
            col1 = int(input("Ingresa la columna de la primera carta (0-4): "))
            # Solicita al jugador la fila y columna de la segunda carta a destapar
            fila2 = int(input("Ingresa la fila de la segunda carta (0-5): "))
            col2 = int(input("Ingresa la columna de la segunda carta (0-4): "))
            
            # Verifica que ambas selecciones sean válidas:
            # 1. Las posiciones estén dentro del rango.
            # 2. No se haya seleccionado la misma carta.
            # 3. Ambas cartas estén ocultas en el tablero.
            if (0 <= fila1 < 6 and 0 <= col1 < 5 and 0 <= fila2 < 6 and 0 <= col2 < 5 and
                (fila1, col1) != (fila2, col2) and tablero_oculto[fila1][col1] == "❓" and tablero_oculto[fila2][col2] == "❓"):
                # Revela las cartas seleccionadas mostrando sus valores reales en el tablero oculto
                tablero_oculto[fila1][col1], tablero_oculto[fila2][col2] = tablero[fila1][col1], tablero[fila2][col2]
                imprimir_tablero(tablero_oculto)  # Imprime el tablero con las dos cartas destapadas
                if tablero[fila1][col1] == tablero[fila2][col2]:
                    print("🎉 ¡Par encontrado!")  # Informa que se encontró un par
                    puntos_jugador += 1  # Actualiza el puntaje del jugador
                    pares_encontrados += 1  # Incrementa el contador de pares encontrados
                else:
                    print("❌ No coinciden. Se vuelven a tapar.")  # Informa que las cartas no coincidieron
                    # Vuelve a ocultar las cartas que no forman un par
                    tablero_oculto[fila1][col1], tablero_oculto[fila2][col2] = "❓", "❓"
                intentos += 1  # Incrementa el número de intentos realizados
            else:
                print("⚠️ Entrada inválida. Asegúrate de elegir cartas diferentes y dentro del rango.")  # Mensaje de error si la entrada es inválida
        except ValueError:
            print("⚠️ Entrada no válida. Ingresa números enteros.")  # Maneja el error en caso de que la entrada no pueda convertirse a entero
        
        # Turno de la máquina
        while True:
            # La máquina selecciona aleatoriamente dos posiciones en el tablero
            fila1, col1, fila2, col2 = random.randint(0, 5), random.randint(0, 4), random.randint(0, 5), random.randint(0, 4)
            # Verifica que las dos posiciones seleccionadas sean diferentes y que ambas estén ocultas
            if (fila1, col1) != (fila2, col2) and tablero_oculto[fila1][col1] == "❓" and tablero_oculto[fila2][col2] == "❓":
                # Revela las cartas seleccionadas por la máquina
                tablero_oculto[fila1][col1], tablero_oculto[fila2][col2] = tablero[fila1][col1], tablero[fila2][col2]
                imprimir_tablero(tablero_oculto)  # Imprime el tablero mostrando las cartas destapadas
                if tablero[fila1][col1] == tablero[fila2][col2]:
                    print("🤖 La máquina encontró un par.")  # Informa que la máquina encontró un par
                    puntos_maquina += 1  # Incrementa el puntaje de la máquina
                    pares_encontrados += 1  # Incrementa el contador global de pares encontrados
                else:
                    print("🤖 La máquina falló. Se vuelven a tapar.")  # Informa que la máquina falló al encontrar un par
                    # Vuelve a ocultar las cartas no coincidentes
                    tablero_oculto[fila1][col1], tablero_oculto[fila2][col2] = "❓", "❓"
                break  # Sale del bucle después de completar el turno de la máquina
        
        contar_manos(intentos)  # Muestra el número de intentos utilizados hasta el momento
        
    print("\n===== FIN DEL JUEGO =====")  # Mensaje de finalización del juego
    # Compara el puntaje del jugador y de la máquina para determinar el ganador
    if puntos_jugador > puntos_maquina:
        print(f"🎉 ¡Ganaste! Descubriste {puntos_jugador} pares contra {puntos_maquina} de la máquina.")  # Mensaje de victoria para el jugador
    elif puntos_jugador < puntos_maquina:
        print(f"🤖 La máquina ganó con {puntos_maquina} pares. ¡Inténtalo de nuevo!")  # Mensaje cuando la máquina gana
    else:
        print(f"🔄 ¡Empate! Ambos encontraron {puntos_jugador} pares.")  # Mensaje en caso de empate

# Programa principal: verifica si el script es ejecutado directamente
if __name__ == "__main__":
    try:
        jugar_memoria()  # Llama a la función principal para iniciar el juego
    except KeyboardInterrupt:
        print("\nHas abandonado la partida. ¡Perdiste!")  # Captura el cierre abrupto del juego