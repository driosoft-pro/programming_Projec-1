# Problema 2: Triqui y Juego de Memoria ❌⭕🃏
```
Diseñe e implemente un programa en Python que permita jugar Triqui y un Juego de Memoria contra la máquina.
```

# Descripción
```
El usuario elige entre jugar Triqui o un Juego de Memoria. 
En Triqui, se turnan con la máquina para marcar posiciones en un tablero de 3x3 hasta que alguien gane o haya empate. 
En el Juego de Memoria, se destapan pares de cartas para encontrar coincidencias.
```

### Triqui
# Pseudocódigo Inicio
```
Inicio
    Escribir "Seleccione un juego: 1. Triqui 2. Juego de Memoria"
    Leer opcion
    
    Si opcion == 1 Entonces
        Iniciar tablero de 3x3 vacío
        Elegir aleatoriamente quién inicia
        
        Repetir hasta que haya un ganador o empate:
            Mostrar tablero
            Si turno del jugador:
                Pedir coordenadas y colocar su símbolo
            Si turno de la máquina:
                Seleccionar una posición válida y colocar su símbolo
            Evaluar si hay un ganador o empate
        
        Mostrar resultado
    
    Sino Si opcion == 2 Entonces
        Crear tablero de 6x5 con pares de figuras aleatorias
        Repetir hasta que todas las parejas sean encontradas:
            Mostrar tablero con pares destapados
            Si turno del jugador:
                Pedir coordenadas para destapar dos figuras
            Si turno de la máquina:
                Elegir dos figuras aleatoriamente
            Si las figuras coinciden, asignar punto
        
        Mostrar ganador
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
        Imprimir "=== ESTAMOS JUGANDO TRIQUI ==="
    FIN FUNCIÓN

    FUNCIÓN mostrar_reglas_triqui()
        Imprimir reglas del juego
    FIN FUNCIÓN

    FUNCIÓN crear_tablero_triqui()
        Crear un tablero vacío de 3x3
        RETORNAR tablero
    FIN FUNCIÓN

    FUNCIÓN imprimir_tablero_triqui(tablero)
        Imprimir encabezado de columnas "    0   1   2"
        Imprimir línea divisoria "  -------------"
        PARA cada fila en el tablero HACER
            Imprimir índice de fila y contenido de la fila
            Imprimir línea divisoria "  -------------"
        FIN PARA
    FIN FUNCIÓN

    FUNCIÓN verificar_ganador(tablero, jugador)
        PARA cada fila en el tablero HACER
            SI todos los elementos de la fila son iguales a jugador ENTONCES
                RETORNAR Verdadero
            FIN SI
        FIN PARA

        PARA cada columna en el tablero HACER
            SI todos los elementos de la columna son iguales a jugador ENTONCES
                RETORNAR Verdadero
            FIN SI
        FIN PARA

        SI todos los elementos de la diagonal principal son iguales a jugador O
           todos los elementos de la diagonal secundaria son iguales a jugador ENTONCES
            RETORNAR Verdadero
        FIN SI

        RETORNAR Falso
    FIN FUNCIÓN

    FUNCIÓN obtener_entrada_usuario()
        MIENTRAS Verdadero HACER
            INTENTAR
                Leer fila y columna desde la entrada del usuario
                SI fila y columna están entre 0 y 2 ENTONCES
                    RETORNAR fila, columna
                SINO
                    Imprimir "Error: Las filas y columnas deben estar entre 0 y 2."
                FIN SI
            CAPTURAR ValueError
                Imprimir "Error: Entrada inválida. Debes ingresar números enteros."
            CAPTURAR KeyboardInterrupt
                Imprimir "Has abandonado el juego."
                Salir del programa
            FIN INTENTAR
        FIN MIENTRAS
    FIN FUNCIÓN

    FUNCIÓN jugar_triqui()
        Mostrar reglas del juego
        Inicializar tablero vacío
        Elegir aleatoriamente quién comienza (jugador o máquina)

        PARA cada turno (máximo 9) HACER
            Limpiar pantalla
            Mostrar título y reglas
            Imprimir tablero

            SI es el turno del jugador ENTONCES
                MIENTRAS Verdadero HACER
                    Obtener fila y columna del usuario
                    SI la celda está vacía ENTONCES
                        Colocar "X" en la celda
                        SI el jugador ha ganado ENTONCES
                            Limpiar pantalla
                            Mostrar título
                            Imprimir tablero
                            Imprimir "¡Felicidades, ganaste!"
                            TERMINAR juego
                        FIN SI
                        Cambiar turno a la máquina
                        SALIR DEL BUCLE
                    SINO
                        Imprimir "Error: La posición ya está ocupada."
                    FIN SI
                FIN MIENTRAS
            SINO
                Elegir aleatoriamente una celda vacía para la máquina
                Colocar "O" en la celda
                SI la máquina ha ganado ENTONCES
                    Limpiar pantalla
                    Mostrar título
                    Imprimir tablero
                    Imprimir "La máquina ha ganado. ¡Inténtalo de nuevo!"
                    TERMINAR juego
                FIN SI
                Cambiar turno al jugador
            FIN SI
        FIN PARA

        SI no hay ganador después de 9 turnos ENTONCES
            Limpiar pantalla
            Mostrar título
            Imprimir tablero
            Imprimir "Es un empate."
        FIN SI
    FIN FUNCIÓN

    PROGRAMA PRINCIPAL
        INTENTAR
            Llamar a la función jugar_triqui()
        CAPTURAR KeyboardInterrupt
            Imprimir "Has abandonado el juego."
        FIN INTENTAR
    FIN PROGRAMA PRINCIPAL
FIN
```

### Memoria
# Pseudocódigo Inicio
```
Inicio
    Definir una matriz de 6x5 "tablero_juego" con 15 pares de figuras colocadas aleatoriamente
    Definir una matriz de 6x5 "tablero_visible" con todas las posiciones ocultas ("*")
    Definir "puntos_jugador" y "puntos_maquina" como 0
    Definir "pares_descubiertos" como 0
    
    Mientras pares_descubiertos < 15 hacer:
        Mostrar "Tablero actual:"
        Mostrar "tablero_visible"

        # Turno del jugador
        Escribir "Turno del jugador. Ingresa las coordenadas de dos cartas para destapar:"
        Leer fila1, columna1
        Leer fila2, columna2
        
        Si las coordenadas ingresadas son válidas y diferentes:
            Mostrar las figuras seleccionadas en "tablero_juego"
            Si las figuras son iguales:
                Escribir "¡Par encontrado!"
                Actualizar "tablero_visible" con las figuras descubiertas
                Incrementar "puntos_jugador" en 1
                Incrementar "pares_descubiertos" en 1
            Sino:
                Escribir "No son iguales. Inténtalo de nuevo."
                Tapar nuevamente las figuras
            
        # Turno de la máquina
        Generar aleatoriamente dos posiciones diferentes "fila1, columna1" y "fila2, columna2"
        Mostrar las figuras seleccionadas en "tablero_juego"
        Si las figuras son iguales:
            Escribir "La máquina encontró un par."
            Actualizar "tablero_visible" con las figuras descubiertas
            Incrementar "puntos_maquina" en 1
            Incrementar "pares_descubiertos" en 1
        Sino:
            Escribir "La máquina no encontró un par."
            Tapar nuevamente las figuras
        
    # Fin del juego
    Escribir "Juego terminado."
    Si "puntos_jugador" > "puntos_maquina" Entonces
        Escribir "¡Felicidades! Ganaste con", puntos_jugador, "pares descubiertos."
    Sino Si "puntos_jugador" < "puntos_maquina" Entonces
        Escribir "La máquina ha ganado con", puntos_maquina, "pares descubiertos."
    Sino
        Escribir "¡Empate! Ambos encontraron la misma cantidad de pares."
Fin
```

# Pseudocódigo Final
```
INICIO
    Importar módulos necesarios (random, os)

    FUNCIÓN mostrar_titulo()
        Imprimir línea separadora superior
        Imprimir título embellecido
        Imprimir línea separadora inferior y salto de línea
    FIN FUNCIÓN

    FUNCIÓN mostrar_reglas()
        Imprimir encabezado de las reglas
        Imprimir reglas del juego
        Imprimir línea inferior de separación
    FIN FUNCIÓN

    FUNCIÓN generar_tablero()
        Definir lista de 15 figuras
        Duplicar la lista para generar pares de cada figura (15 pares en total)
        Mezclar aleatoriamente la lista de figuras
        Crear y devolver una matriz de 6 filas y 5 columnas
    FIN FUNCIÓN

    FUNCIÓN generar_tablero_oculto()
        Retornar una lista de 6 listas, cada una con 5 "❓"
    FIN FUNCIÓN

    FUNCIÓN imprimir_tablero(tablero)
        Imprimir índices de las columnas
        PARA cada fila en el tablero HACER
            Imprimir índice de la fila y los elementos de la misma separados por espacios
        FIN PARA
    FIN FUNCIÓN

    FUNCIÓN contar_manos(intentos)
        Imprimir número de intentos utilizados
    FIN FUNCIÓN

    FUNCIÓN jugar_memoria()
        Mostrar título del juego
        Mostrar reglas del juego
        
        Crear tablero con las figuras ya mezcladas
        Crear tablero de visualización con todas las cartas ocultas
        Inicializar puntajes para el jugador, la máquina y la cantidad de intentos
        Inicializar contador de pares encontrados
        
        MIENTRAS pares_encontrados < 15 HACER
            Mostrar estado actual del tablero oculto
            
            INTENTAR
                Solicitar al jugador la fila y columna de la primera carta a destapar
                Solicitar al jugador la fila y columna de la segunda carta a destapar
                
                SI las selecciones son válidas ENTONCES
                    Revelar las cartas seleccionadas mostrando sus valores reales en el tablero oculto
                    Imprimir el tablero con las dos cartas destapadas
                    SI las cartas coinciden ENTONCES
                        Informar que se encontró un par
                        Actualizar puntaje del jugador
                        Incrementar contador de pares encontrados
                    SINO
                        Informar que las cartas no coincidieron
                        Volver a ocultar las cartas que no forman un par
                    FIN SI
                    Incrementar número de intentos realizados
                SINO
                    Imprimir mensaje de error
                FIN SI
            CAPTURAR ValueError
                Imprimir mensaje de error
            CAPTURAR KeyboardInterrupt
                Imprimir mensaje de cierre abrupto
                Salir del programa
            FIN INTENTAR
            
            // Turno de la máquina
            MIENTRAS Verdadero HACER
                Seleccionar aleatoriamente dos posiciones en el tablero
                SI las dos posiciones seleccionadas sean diferentes y ambas estén ocultas ENTONCES
                    Revelar las cartas seleccionadas por la máquina
                    Imprimir el tablero mostrando las cartas destapadas
                    SI las cartas coinciden ENTONCES
                        Informar que la máquina encontró un par
                        Incrementar puntaje de la máquina
                        Incrementar contador global de pares encontrados
                    SINO
                        Informar que la máquina falló al encontrar un par
                        Volver a ocultar las cartas no coincidentes
                    FIN SI
                    SALIR DEL BUCLE
                FIN SI
            FIN MIENTRAS
            
            Mostrar número de intentos utilizados hasta el momento
        FIN MIENTRAS
        
        Imprimir mensaje de finalización del juego
        Comparar puntaje del jugador y de la máquina para determinar el ganador
    FIN FUNCIÓN

    PROGRAMA PRINCIPAL
        INTENTAR
            Llamar a la función jugar_memoria()
        CAPTURAR KeyboardInterrupt
            Imprimir mensaje de cierre abrupto
        FIN INTENTAR
    FIN PROGRAMA PRINCIPAL
FIN
```