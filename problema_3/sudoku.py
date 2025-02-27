import random  # Importa la librería random para generar números aleatorios
import os  # Importa el módulo os para interactuar con el sistema operativo, por ejemplo, para limpiar la pantalla

# Función para limpiar la pantalla de la consola.
def limpiar_pantalla():
    if os.name == "nt":  # Verifica si el sistema operativo es Windows
        os.system("cls")  # Ejecuta el comando "cls" para limpiar la pantalla en Windows
    else:
        os.system("clear")  # Ejecuta el comando "clear" para limpiar la pantalla en sistemas tipo Unix

# Función para mostrar el título del juego.
def mostrar_titulo():
    print("=== === === === === ESTAMOS JUGANDO SUDOKU === === === === ===")  # Imprime el título del juego y un salto de línea al final

# ======================= SUDOKU =======================
# Funciones que implementan la lógica de un juego de Sudoku 9x9.

def mostrar_reglas_sudoku():
    # Imprime el encabezado para las reglas de Sudoku, iniciando con salto de línea
    print("\n====================== REGLAS DE SUDOKU ======================")  # Muestra el título de la sección de reglas

    # Imprime la regla que indica que se selecciona aleatoriamente un tablero incompleto
    print("- Se elige aleatoriamente un tablero de Sudoku 9x9 incompleto.")  # Explica que el tablero se selecciona de forma aleatoria

    # Imprime la regla que indica que el jugador debe completar los espacios vacíos con números del 1 al 9
    print("- Debes completar los espacios vacíos con números del 1 al 9.")  # Indica que se deben rellenar los huecos (vacíos)

    # Imprime la regla que prohíbe la repetición de números en las filas y columnas
    print("- No puede haber números repetidos en filas ni columnas.")  # Resalta que no se pueden repetir números en ninguna fila o columna

    # Imprime la regla que establece como condición de victoria completar correctamente el tablero
    print("- Ganas si completas correctamente el tablero.")  # Establece el objetivo: completar el tablero siguiendo las reglas

    # Imprime una línea divisoria final y un salto de línea para finalizar la sección de reglas
    print("===============================================================\n")  # Cierra la sección de reglas

# Define la función generar_tablero_sudoku(), la cual crea un tablero de Sudoku 9x9 incompleto.
def generar_tablero_sudoku():
    tablero = [[" " for _ in range(9)] for _ in range(9)]  # Crea una matriz 9x9 inicializada con espacios en blanco
    for i in range(9):  # Itera sobre cada fila del tablero (índice 0 a 8)
        for j in range(9):  # Itera sobre cada columna de la fila (índice 0 a 8)
            num = random.randint(1, 9)  # Genera un número aleatorio entre 1 y 9
            # Repite la generación de 'num' hasta asegurarse de que no se repita en la fila i ni en la columna j
            while num in tablero[i] or any(row[j] == num for row in tablero):
                num = random.randint(1, 9)  # Genera un nuevo número aleatorio si ya está en la fila o columna
            if random.random() > 0.5:  # Con una probabilidad del 50%, se asigna el número a la posición (i, j)
                tablero[i][j] = num  # Asigna el número generado a la celda (i, j)
    return tablero  # Retorna el tablero generado

# Define la función imprimir_tablero_sudoku() para mostrar el tablero en consola.
def imprimir_tablero_sudoku(tablero):
    # Imprime la cabecera de columnas (índices del 0 al 8) con separación
    print("    " + "   ".join(str(i) for i in range(9)))  # Cabecera con números de columna
    print("  " + "----" * 9)  # Imprime una línea divisoria debajo de la cabecera
    for i, fila in enumerate(tablero):  # Itera sobre cada fila del tablero con su índice
        # Imprime el índice de la fila seguido de las celdas separadas por barras
        print(f"{i} | " + " | ".join(str(c) for c in fila) + " |")  # Muestra la fila con celdas delimitadas por barras
        print("  " + "----" * 9)  # Imprime una línea divisoria luego de cada fila

# Define la función verificar_sudoku() que comprueba si el tablero ha sido completado.
def verificar_sudoku(tablero):
    for fila in tablero:  # Itera sobre cada fila del tablero
        if any(c == " " for c in fila):  # Verifica si existe alguna celda vacía (representada por un espacio)
            return False  # Si hay un espacio vacío, devuelve False indicando que el tablero no está completo
    return True  # Si no se encuentran celdas vacías, devuelve True (tablero completo)

# Define la función obtener_entrada_usuario() para solicitar al jugador una jugada válida.
def obtener_entrada_usuario():
    while True:  # Bucle que se repite hasta obtener una entrada válida
        try:
            fila = int(input("Ingresa la fila (0-8): "))  # Solicita y convierte la entrada de fila a entero
            columna = int(input("Ingresa la columna (0-8): "))  # Solicita y convierte la entrada de columna a entero
            numero = int(input("Ingresa un número (1-9): "))  # Solicita y convierte la entrada del número a entero
            
            if 0 <= fila <= 8 and 0 <= columna <= 8:  # Verifica que fila y columna estén dentro del rango permitido
                if 1 <= numero <= 9:  # Verifica que el número esté dentro del rango permitido (1-9)
                    return fila, columna, numero  # Retorna la entrada válida (fila, columna y número)
                else:
                    print("Error: El número debe estar entre 1 y 9. Intenta de nuevo.")  # Mensaje de error para número incorrecto
            else:
                print("Error: La fila y columna deben estar entre 0 y 8. Intenta de nuevo.")  # Mensaje de error si fila o columna están fuera de rango
        except ValueError:
            # Captura error si la entrada no es convertible a entero y muestra un mensaje
            print("Error: Entrada inválida. Debes ingresar números enteros. Intenta de nuevo.")
        except KeyboardInterrupt:
            # Captura si el usuario interrumpe la ejecución (Ctrl+C) y finaliza el juego
            print("\nHas abandonado el juego.")
            exit()

# Define la función jugar_sudoku() que contiene la lógica principal del juego.
def jugar_sudoku():
    mostrar_reglas_sudoku()  # Llama a la función que muestra las reglas del Sudoku
    tablero = generar_tablero_sudoku()  # Genera un tablero de Sudoku aleatorio e incompleto
    
    # Mientras el tablero no esté completo, sigue solicitando entradas al usuario
    while not verificar_sudoku(tablero):
        limpiar_pantalla()  # Limpia la pantalla para refrescar la vista del juego
        mostrar_titulo()  # Muestra el título del juego
        mostrar_reglas_sudoku()  # Vuelve a mostrar las reglas de Sudoku
        imprimir_tablero_sudoku(tablero)  # Imprime el estado actual del tablero
        
        while True:  # Bucle interno para solicitar al jugador una jugada válida
            try:
                fila, columna, numero = obtener_entrada_usuario()  # Obtiene la entrada del usuario
                if tablero[fila][columna] == " ":  # Comprueba si la celda seleccionada está vacía
                    # Verifica si el número ingresado no se repite en la fila ni en la columna
                    if numero not in tablero[fila] and all(row[columna] != numero for row in tablero):
                        tablero[fila][columna] = numero  # Asigna el número a la celda seleccionada
                        break  # Sale del bucle interno tras una jugada exitosa
                    else:
                        # Informa al usuario que no puede repetir números en la misma fila o columna
                        print("Error: No puedes repetir números en la misma fila o columna. Intenta de nuevo.")
                else:
                    # Informa al jugador que la celda ya ha sido ocupada
                    print("Error: La celda ya está ocupada. Intenta de nuevo.")
            except Exception as e:
                # Captura cualquier error inesperado y lo muestra
                print(f"Error inesperado: {e}. Intenta de nuevo.")
    
    limpiar_pantalla()  # Limpia la pantalla una vez completado el tablero
    mostrar_titulo()  # Muestra nuevamente el título del juego
    imprimir_tablero_sudoku(tablero)  # Imprime el tablero completo final
    print("\n¡Felicidades, completaste el Sudoku!")  # Muestra un mensaje de felicitación

# Si el script es ejecutado directamente, inicia el juego de Sudoku.
if __name__ == "__main__":
    try:
        jugar_sudoku()  # Llama a la función principal para comenzar el juego
    except KeyboardInterrupt:
        # Si se interrumpe la ejecución (Ctrl+C), muestra un mensaje de salida
        print("\nHas abandonado el juego.")