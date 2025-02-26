# Problema 1: Batalla Naval 🚢
```
Diseñe e implemente una versión del juego Batalla Naval en Python, donde el jugador compite contra la máquina en un tablero de 5x5. Cada jugador tendrá tres barcos que ocuparán una única posición en la matriz. Gana quien hunda primero los tres barcos del oponente.
```

# Descripción
```
El juego consiste en colocar barcos en un tablero de 5x5. La máquina posiciona sus barcos aleatoriamente, mientras que el jugador humano los ubica ingresando coordenadas. En cada turno, la máquina y el jugador atacan, intentando acertar en las posiciones enemigas. El juego finaliza cuando un jugador hunde los tres barcos del oponente.
```

# Pseudocódigo Inicial
```
Inicio
    Crear tablero de 5x5 para el jugador y la máquina
    Colocar tres barcos de la máquina en posiciones aleatorias
    Pedir al jugador que ingrese las coordenadas de sus tres barcos
    
    Repetir hasta que un jugador hunda los tres barcos del oponente:
        Mostrar tableros de juego
        Pedir al jugador que ingrese coordenadas para atacar
        Evaluar si el ataque del jugador acertó en un barco de la máquina
        
        Generar ataque aleatorio de la máquina
        Evaluar si el ataque de la máquina acertó en un barco del jugador
        
        Mostrar el resultado de los ataques
    
    Si el jugador hunde los tres barcos de la máquina
        Escribir "¡Ganaste la batalla naval!"
    Sino
        Escribir "¡La máquina ha ganado la batalla naval!"
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
        Imprimir "=== ESTAMOS JUGANDO BATALLA NAVAL ==="
    FIN FUNCIÓN

    FUNCIÓN mostrar_reglas_batalla_naval()
        Imprimir reglas del juego
    FIN FUNCIÓN

    FUNCIÓN crear_tablero()
        Crear y retornar un tablero vacío de 5x5
    FIN FUNCIÓN

    FUNCIÓN imprimir_tablero(tablero)
        Imprimir encabezado de columnas (0 al 4)
        PARA cada fila en el tablero HACER
            Imprimir índice de la fila y las celdas separadas por espacios
        FIN PARA
    FIN FUNCIÓN

    FUNCIÓN colocar_barcos(tablero, cantidad)
        Inicializar contador de barcos colocados en 0
        MIENTRAS barcos_colocados < cantidad HACER
            Generar aleatoriamente fila y columna entre 0 y 4
            SI la celda en (fila, columna) está vacía ENTONCES
                Colocar un barco ("B") en la celda
                Incrementar contador de barcos colocados
            FIN SI
        FIN MIENTRAS
    FIN FUNCIÓN

    FUNCIÓN colocar_barcos_jugador(tablero)
        Inicializar contador de barcos colocados en 0
        MIENTRAS barcos_colocados < 3 HACER
            INTENTAR
                Solicitar fila y columna al jugador
                SI fila y columna están entre 0 y 4 Y la celda está vacía ENTONCES
                    Colocar un barco ("B") en la celda
                    Incrementar contador de barcos colocados
                SINO
                    Imprimir "Posición inválida o ya ocupada, intenta de nuevo."
                FIN SI
            CAPTURAR ValueError
                Imprimir "Entrada inválida, ingresa números entre 0 y 4."
            CAPTURAR KeyboardInterrupt
                Imprimir "Has abandonado la partida. ¡Perdiste!"
                Salir del programa
            FIN INTENTAR
        FIN MIENTRAS
    FIN FUNCIÓN

    FUNCIÓN contar_intentos(intentos)
        Imprimir número de intentos realizados
    FIN FUNCIÓN

    FUNCIÓN jugar_batalla_naval()
        Mostrar reglas del juego
        Crear tablero del jugador
        Crear tablero de la máquina
        Crear tablero de ataques
        
        Solicitar al jugador que coloque sus barcos
        Colocar barcos de la máquina aleatoriamente
        
        Inicializar contadores de barcos restantes (jugador y máquina)
        Inicializar contador de intentos en 0
        
        MIENTRAS ambos jugadores tengan barcos restantes HACER
            Limpiar pantalla
            Mostrar título
            Mostrar reglas
            Imprimir tablero de ataques
            Mostrar número de intentos
            
            // Turno del jugador
            INTENTAR
                Solicitar fila y columna para atacar
                SI las coordenadas están dentro del rango ENTONCES
                    SI hay un barco enemigo en la celda ENTONCES
                        Marcar celda como hundida ("X")
                        Reducir contador de barcos de la máquina
                        Imprimir "¡Impacto! Hundiste un barco enemigo."
                    SINO
                        Marcar celda como fallo ("O")
                        Imprimir "Agua. No impactaste ningún barco."
                    FIN SI
                    Incrementar contador de intentos
                SINO
                    Imprimir "Coordenadas fuera de rango."
                FIN SI
            CAPTURAR ValueError
                Imprimir "Entrada inválida, ingresa números entre 0 y 4."
            CAPTURAR KeyboardInterrupt
                Imprimir "Has abandonado la partida. ¡Perdiste!"
                Salir del programa
            FIN INTENTAR
            
            // Turno de la máquina
            SI la máquina tiene barcos restantes ENTONCES
                Seleccionar aleatoriamente fila y columna para atacar
                SI hay un barco del jugador en la celda ENTONCES
                    Marcar celda como hundida ("X")
                    Reducir contador de barcos del jugador
                    Imprimir "La máquina atacó (fila, columna) y hundió uno de tus barcos."
                SINO
                    Imprimir "La máquina atacó (fila, columna) pero falló."
                FIN SI
            FIN SI
        FIN MIENTRAS
        
        Limpiar pantalla
        Mostrar título
        SI el jugador no tiene barcos restantes ENTONCES
            Imprimir "La máquina ha ganado la Batalla Naval. ¡Mejor suerte la próxima vez!"
        SINO
            Imprimir "¡Felicidades! Has ganado la Batalla Naval."
        FIN SI
    FIN FUNCIÓN

    PROGRAMA PRINCIPAL
        INTENTAR
            Llamar a la función jugar_batalla_naval()
        CAPTURAR KeyboardInterrupt
            Imprimir "Has abandonado la partida. ¡Perdiste!"
        FIN INTENTAR
    FIN PROGRAMA PRINCIPAL
FIN
```