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
    print("=== ESTAMOS JUGANDO SUDOKU ===\n")  # Imprime el título del juego y un salto de línea al final

# ======================= SUDOKU =======================
# Funciones que implementan la lógica de un juego de Sudoku 9x9.

def mostrar_reglas_sudoku():
    print("\n===== REGLAS DE SUDOKU =====")  # Imprime el encabezado para las reglas, con un salto de línea inicial
    print("- Se elige aleatoriamente un tablero de Sudoku 9x9 incompleto.")  # Explica que se selecciona un tablero incompleto al azar
    print("- Debes completar los espacios vacíos con números del 1 al 9.")  # Indica que el jugador debe llenar los espacios vacíos con números del 1 al 9
    print("- No puede haber números repetidos en filas ni columnas.")  # Resalta la regla de que no se pueden repetir números en una misma fila o columna
    print("- Ganas si completas correctamente el tablero.")  # Establece la condición de victoria al completar el tablero correctamente
    print("===================================\n")  # Imprime una línea de cierre para las reglas y agrega un salto de línea

def generar_tablero_sudoku():
    tableros = [  # Crea una lista que contiene uno o más tableros
        [[random.randint(1, 9) if random.random() > 0.5 else " " for _ in range(9)] for _ in range(9)]
        # Para cada uno de los 9 renglones, crea una lista de 9 celdas. Cada celda obtiene un número aleatorio del 1 al 9 
        # si random.random() genera un número mayor a 0.5; de lo contrario, se deja vacío (" ").
    ]
    return random.choice(tableros)  # Selecciona y retorna aleatoriamente uno de los tableros creados en la lista

def imprimir_tablero_sudoku(tablero):
    print("    " + "   ".join(str(i) for i in range(9)))  # Imprime la cabecera de columnas (0 al 8) con espacios y separadores
    print("  " + "----" * 9)  # Imprime una línea divisoria debajo de la cabecera
    for i, fila in enumerate(tablero):  # Itera sobre cada fila del tablero, obteniendo su índice y contenido
        print(f"{i} | " + " | ".join(str(c) for c in fila) + " |")  # Imprime el índice de la fila seguido de sus celdas separadas por barras
        print("  " + "----" * 9)  # Imprime una línea divisoria después de cada fila

def verificar_sudoku(tablero):
    for fila in tablero:  # Recorre cada fila del tablero
        if any(c == " " for c in fila):  # Comprueba si existe alguna celda vacía (" ") en la fila
            return False  # Si se encuentra una celda vacía, retorna False, indicando que el Sudoku no está completo
    return True  # Si ninguna fila contiene celdas vacías, retorna True para indicar que el tablero está completo

def obtener_entrada_usuario():
    while True:  # Bucle que se repite hasta que se ingrese una entrada válida
        try:
            fila = int(input("Ingresa la fila (0-8): "))  # Solicita al usuario el número de fila (entre 0 y 8) y lo convierte a entero
            columna = int(input("Ingresa la columna (0-8): "))  # Solicita el número de columna (entre 0 y 8) y lo convierte a entero
            numero = int(input("Ingresa un número (1-9): "))  # Solicita el número que se desea colocar (entre 1 y 9) y lo convierte a entero
            
            if 0 <= fila <= 8 and 0 <= columna <= 8:  # Verifica que la fila y la columna estén dentro del rango permitido
                if 1 <= numero <= 9:  # Verifica que el número ingresado esté entre 1 y 9
                    return fila, columna, numero  # Retorna la entrada válida (fila, columna, número)
                else:
                    print("Error: El número debe estar entre 1 y 9. Intenta de nuevo.")  # Muestra error si el número no está en el rango permitido
            else:
                print("Error: La fila y columna deben estar entre 0 y 8. Intenta de nuevo.")  # Muestra error si la fila o columna no están en el rango permitido
        except ValueError:
            print("Error: Entrada inválida. Debes ingresar números enteros. Intenta de nuevo.")  # Muestra error si la entrada no es convertible a entero
        except KeyboardInterrupt:
            print("\nHas abandonado el juego.")  # Muestra un mensaje si el usuario interrumpe el juego con Ctrl+C
            exit()  # Termina la ejecución del programa

def jugar_sudoku():
    mostrar_reglas_sudoku()  # Muestra las reglas del Sudoku al iniciar el juego
    tablero = generar_tablero_sudoku()  # Genera un tablero de Sudoku 9x9 incompleto aleatoriamente
    
    while not verificar_sudoku(tablero):  # Mientras el tablero no esté completo, se continúa solicitando entradas
        limpiar_pantalla()  # Limpia la pantalla para refrescar la vista del juego
        mostrar_titulo()  # Muestra el título del juego
        mostrar_reglas_sudoku()  # Vuelve a mostrar las reglas para recordarle al jugador las reglas del juego
        imprimir_tablero_sudoku(tablero)  # Imprime el estado actual del tablero
        
        while True:  # Bucle interno para continuar solicitando una jugada válida en la celda seleccionada
            try:
                fila, columna, numero = obtener_entrada_usuario()  # Obtiene la entrada del usuario (fila, columna, número)
                if tablero[fila][columna] == " ":  # Verifica si la celda elegida está vacía
                    tablero[fila][columna] = numero  # Actualiza la celda del tablero con el número ingresado
                    break  # Sale del bucle interno después de haber realizado una jugada exitosa
                else:
                    print("Error: La celda ya está ocupada. Intenta de nuevo.")  # Muestra error si la celda ya contiene un valor
            except Exception as e:
                print(f"Error inesperado: {e}. Intenta de nuevo.")  # Maneja y muestra errores inesperados durante la entrada
    
    limpiar_pantalla()  # Una vez completado el tablero, limpia la pantalla para la etapa final
    mostrar_titulo()  # Muestra el título del juego nuevamente
    imprimir_tablero_sudoku(tablero)  # Imprime el tablero completo ya finalizado
    print("\n¡Felicidades, completaste el Sudoku!")  # Muestra un mensaje de felicitación al jugador por completar el Sudoku

if __name__ == "__main__":  # Verifica si el script se está ejecutando como programa principal
    try:
        jugar_sudoku()  # Llama a la función principal para iniciar el juego de Sudoku
    except KeyboardInterrupt:
        print("\nHas abandonado el juego.")  # Captura la interrupción por teclado (Ctrl+C) durante la ejecución y muestra un mensaje