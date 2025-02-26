# Problema 3: Sudoku 🔢
```
Diseñe e implemente un juego de Sudoku en Python, donde el usuario debe completar un tablero de nivel fácil escogido aleatoriamente.
```

# Descripción
```
El programa selecciona un tablero de Sudoku entre cinco opciones disponibles. El usuario ingresa valores en coordenadas seleccionadas. Al final, se verifica si el tablero fue completado correctamente.
```

# Pseudocódigo Inical
```
Inicio
    Cargar cinco tableros de Sudoku de nivel fácil
    Seleccionar uno de forma aleatoria
    
    Repetir hasta que el tablero esté completo:
        Mostrar el tablero
        Pedir al usuario una coordenada y un número
        Verificar si la casilla está ocupada
        Si está vacía, colocar el número
        
        Si el tablero está lleno, verificar si es correcto
    
    Si el tablero es correcto
        Escribir "¡Felicidades, completaste el Sudoku!"
    Sino
        Escribir "Hay errores en el tablero. Sigue intentando."
Fin
```


# Pseudocódigo Final
```
INICIO
    Importar módulos necesarios (random, os)

    FUNCIÓN limpiar_pantalla()
        SI sistema operativo es Windows ENTONCES
            Ejecutar comando "cls"
        SINO
            Ejecutar comando "clear"
        FIN SI
    FIN FUNCIÓN

    FUNCIÓN mostrar_titulo()
        Imprimir "=== ESTAMOS JUGANDO SUDOKU ===\n"
    FIN FUNCIÓN

    FUNCIÓN mostrar_reglas_sudoku()
        Imprimir reglas del juego
    FIN FUNCIÓN

    FUNCIÓN generar_tablero_sudoku()
        Crear lista de tableros con celdas aleatorias (números del 1 al 9 o vacías)
        Retornar un tablero seleccionado al azar
    FIN FUNCIÓN

    FUNCIÓN imprimir_tablero_sudoku(tablero)
        Imprimir cabecera de columnas (0 al 8)
        Imprimir línea divisoria
        PARA cada fila en el tablero HACER
            Imprimir índice de la fila y sus celdas separadas por barras
            Imprimir línea divisoria
        FIN PARA
    FIN FUNCIÓN

    FUNCIÓN verificar_sudoku(tablero)
        PARA cada fila en el tablero HACER
            SI alguna celda está vacía ENTONCES
                RETORNAR Falso
            FIN SI
        FIN PARA
        RETORNAR Verdadero
    FIN FUNCIÓN

    FUNCIÓN obtener_entrada_usuario()
        MIENTRAS Verdadero HACER
            INTENTAR
                Leer fila, columna y número desde la entrada del usuario
                SI fila y columna están entre 0 y 8 ENTONCES
                    SI número está entre 1 y 9 ENTONCES
                        RETORNAR fila, columna, número
                    SINO
                        Imprimir "Error: El número debe estar entre 1 y 9."
                    FIN SI
                SINO
                    Imprimir "Error: La fila y columna deben estar entre 0 y 8."
                FIN SI
            CAPTURAR ValueError
                Imprimir "Error: Entrada inválida. Debes ingresar números enteros."
            CAPTURAR KeyboardInterrupt
                Imprimir "Has abandonado el juego."
                Salir del programa
            FIN INTENTAR
        FIN MIENTRAS
    FIN FUNCIÓN

    FUNCIÓN jugar_sudoku()
        Mostrar reglas del juego
        Generar tablero de Sudoku incompleto
        
        MIENTRAS el tablero no esté completo HACER
            Limpiar pantalla
            Mostrar título
            Mostrar reglas
            Imprimir tablero
            
            MIENTRAS Verdadero HACER
                Obtener fila, columna y número del usuario
                SI la celda seleccionada está vacía ENTONCES
                    Actualizar celda con el número ingresado
                    SALIR DEL BUCLE
                SINO
                    Imprimir "Error: La celda ya está ocupada."
                FIN SI
            FIN MIENTRAS
        FIN MIENTRAS
        
        Limpiar pantalla
        Mostrar título
        Imprimir tablero
        Imprimir "¡Felicidades, completaste el Sudoku!"
    FIN FUNCIÓN

    PROGRAMA PRINCIPAL
        INTENTAR
            Llamar a la función jugar_sudoku()
        CAPTURAR KeyboardInterrupt
            Imprimir "Has abandonado el juego."
        FIN INTENTAR
    FIN PROGRAMA PRINCIPAL
FIN
```