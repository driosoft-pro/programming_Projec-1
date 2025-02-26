import random  # Importa el módulo random para operaciones aleatorias
import os  # Importa el módulo os para limpiar la pantalla

# ======================= JUEGO DE MEMORIA =======================
# (Comentario: Sección principal del juego de memoria)

def mostrar_titulo():
    # Función para mostrar el título del juego de memoria.
    print("\n=======================================================")  # Imprime una línea separadora
    print(" === === === === 🎴 JUEGO DE MEMORIA 🎴 === === === ===")  # Imprime el título decorado
    print("=======================================================\n")  # Imprime la línea separadora final y un salto de línea

def mostrar_reglas():
    # Función para mostrar las reglas del juego de memoria.
    print("\n============ REGLAS DEL JUEGO DE MEMORIA ============")  # Imprime el encabezado de las reglas
    print("- Tablero de 6x5 con 15 pares de figuras ocultas.")  # Explica el tamaño del tablero y el número de pares
    print("- Encuentra los pares destapando dos cartas por turno.")  # Indica la mecánica del juego: elegir dos cartas
    print("- Si aciertas, el par queda visible y ganas un punto.")  # Explica la recompensa por acertar el par
    print("- Si fallas, las cartas se vuelven a tapar.")  # Explica que las cartas se vuelven a ocultar si no coinciden
    print("- Gana quien descubra más pares.")  # Establece la condición de victoria
    print("=======================================================\n")  # Imprime la línea final de las reglas

def generar_tablero():
    # Función para generar el tablero completo con las figuras.
    figuras = ["🍎", "🍌", "🍉", "🍓", "🍒", "🥝", "🍇", "🍍", "🥕", "🌽", "🥑", "🥥", "🍄", "🥒", "🌶"]  # Lista con 15 figuras
    figuras *= 2  # Duplica la lista para tener 15 pares
    random.shuffle(figuras)  # Mezcla aleatoriamente las figuras
    return [figuras[i * 5:(i + 1) * 5] for i in range(6)]  # Crea y retorna una matriz 6x5 a partir de la lista de figuras

def generar_tablero_oculto():
    # Función para generar el tablero que se muestra al usuario con las cartas ocultas ("❓")
    return [["❓"] * 5 for _ in range(6)]  # Retorna una matriz 6x5 llena de "❓"

def imprimir_tablero(tablero):
    # Función para imprimir el tablero actual en la consola.
    print("  0 1 2 3 4")  # Imprime los índices de las columnas
    for i, fila in enumerate(tablero):  # Itera sobre cada fila del tablero con su índice
        print(i, " ".join(fila))  # Imprime el índice de la fila y sus elementos separados por espacios

def contar_manos(intentos, aciertos_jugador, errores_jugador, aciertos_maquina, errores_maquina):
    # Función para mostrar estadísticas: intentos usados, aciertos y errores del jugador y la máquina.
    print(f"\n🃏 Intentos usados: {intentos}")  # Muestra el número de intentos realizados
    print(f"👤 Jugador - Aciertos: {aciertos_jugador}, Errores: {errores_jugador}")  # Muestra el desempeño del jugador
    print(f"🤖 Máquina - Aciertos: {aciertos_maquina}, Errores: {errores_maquina}\n")  # Muestra el desempeño de la máquina

def jugar_memoria():
    # Función principal que ejecuta el juego de memoria.
    mostrar_titulo()  # Llama a la función que muestra el título del juego
    mostrar_reglas()  # Llama a la función que muestra las reglas del juego
    
    tablero = generar_tablero()  # Genera el tablero real con las figuras
    tablero_oculto = generar_tablero_oculto()  # Genera el tablero visible inicialmente con todas las cartas ocultas
    puntos_jugador, puntos_maquina, intentos = 0, 0, 0  # Inicializa puntajes y contador de intentos
    aciertos_jugador, errores_jugador, aciertos_maquina, errores_maquina = 0, 0, 0, 0  # Inicializa contadores de jugadas correctas e incorrectas para ambos
    pares_encontrados = 0  # Inicializa el contador de pares encontrados
    
    while pares_encontrados < 15:  # Bucle principal: continúa hasta encontrar los 15 pares
        imprimir_tablero(tablero_oculto)  # Imprime el estado actual del tablero visible
        
        try:
            print("\nTu turno: Elige dos cartas para destapar.")  # Pide al usuario que elija dos cartas
            fila1 = int(input("Ingresa la fila de la primera carta (0-5): "))  # Lee y convierte la fila de la primera carta
            col1 = int(input("Ingresa la columna de la primera carta (0-4): "))  # Lee y convierte la columna de la primera carta
            fila2 = int(input("Ingresa la fila de la segunda carta (0-5): "))  # Lee y convierte la fila de la segunda carta
            col2 = int(input("Ingresa la columna de la segunda carta (0-4): "))  # Lee y convierte la columna de la segunda carta
            
            # Verifica que las coordenadas estén en rango, sean distintas y que ambas cartas estén ocultas.
            if (0 <= fila1 < 6 and 0 <= col1 < 5 and 0 <= fila2 < 6 and 0 <= col2 < 5 and
                (fila1, col1) != (fila2, col2) and tablero_oculto[fila1][col1] == "❓" and tablero_oculto[fila2][col2] == "❓"):
                # Revela las cartas seleccionadas al actualizar el tablero visible con las figuras correspondientes.
                tablero_oculto[fila1][col1], tablero_oculto[fila2][col2] = tablero[fila1][col1], tablero[fila2][col2]
                imprimir_tablero(tablero_oculto)  # Imprime el tablero con las cartas destapadas
                
                if tablero[fila1][col1] == tablero[fila2][col2]:
                    print("🎉 ¡Par encontrado!")  # Si las cartas coinciden, informa que se encontró un par
                    puntos_jugador += 1  # Incrementa el puntaje del jugador
                    aciertos_jugador += 1  # Incrementa el contador de aciertos del jugador
                    pares_encontrados += 1  # Incrementa el contador global de pares encontrados
                else:
                    print("❌ No coinciden. Se vuelven a tapar.")  # Si no coinciden, informa el fallo
                    # Vuelve a ocultar las cartas cambiándolas de nuevo por "❓"
                    tablero_oculto[fila1][col1], tablero_oculto[fila2][col2] = "❓", "❓"
                    errores_jugador += 1  # Incrementa el contador de errores del jugador
                intentos += 1  # Incrementa el conteo total de intentos
            else:
                print("⚠️ Entrada inválida. Asegúrate de elegir cartas diferentes y dentro del rango.")  # Mensaje en caso de entrada inválida
        except ValueError:
            # Captura el error si la entrada no es un entero y muestra un mensaje de advertencia.
            print("⚠️ Entrada no válida. Ingresa números enteros.")
        
        while True:
            # Turno de la máquina: selecciona aleatoriamente dos cartas.
            fila1, col1, fila2, col2 = random.randint(0, 5), random.randint(0, 4), random.randint(0, 5), random.randint(0, 4)
            # Verifica que las cartas seleccionadas sean diferentes y que ambas estén ocultas.
            if (fila1, col1) != (fila2, col2) and tablero_oculto[fila1][col1] == "❓" and tablero_oculto[fila2][col2] == "❓":
                # Revela las cartas elegidas por la máquina en el tablero visible.
                tablero_oculto[fila1][col1], tablero_oculto[fila2][col2] = tablero[fila1][col1], tablero[fila2][col2]
                imprimir_tablero(tablero_oculto)  # Muestra el tablero con las cartas destapadas
                if tablero[fila1][col1] == tablero[fila2][col2]:
                    print("🤖 La máquina encontró un par.")  # Informa que la máquina encontró un par
                    puntos_maquina += 1  # Incrementa el puntaje de la máquina
                    aciertos_maquina += 1  # Incrementa el contador de aciertos de la máquina
                    pares_encontrados += 1  # Incrementa el contador global de pares encontrados
                else:
                    print("🤖 La máquina falló. Se vuelven a tapar.")  # Informa que la máquina no encontró un par
                    # Oculta de nuevo las cartas que no coinciden
                    tablero_oculto[fila1][col1], tablero_oculto[fila2][col2] = "❓", "❓"
                    errores_maquina += 1  # Incrementa el contador de errores de la máquina
                break  # Sale del bucle tras realizar el turno de la máquina
        
        contar_manos(intentos, aciertos_jugador, errores_jugador, aciertos_maquina, errores_maquina)  # Muestra las estadísticas actuales de la partida
        
    print("\n===== FIN DEL JUEGO =====")  # Informa que el juego ha terminado
    if puntos_jugador > puntos_maquina:
        print(f"🎉 ¡Ganaste! Descubriste {puntos_jugador} pares contra {puntos_maquina} de la máquina.")  # Mensaje de victoria para el jugador
    elif puntos_jugador < puntos_maquina:
        print(f"🤖 La máquina ganó con {puntos_maquina} pares. ¡Inténtalo de nuevo!")  # Mensaje de derrota para el jugador
    else:
        print(f"🔄 ¡Empate! Ambos encontraron {puntos_jugador} pares.")  # Mensaje en caso de empate

# Programa principal: se ejecuta solo si este script se invoca directamente.
if __name__ == "__main__":
    try:
        jugar_memoria()  # Inicia el juego llamando a la función principal jugar_memoria()
    except KeyboardInterrupt:
        # Captura la interrupción por teclado (Ctrl+C) para finalizar el juego de forma controlada.
        print("\nHas abandonado la partida. ¡Perdiste!")
