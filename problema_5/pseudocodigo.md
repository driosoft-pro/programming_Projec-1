# Problema 5: Rummy 🃏
```
Diseñe e implemente una versión simplificada del juego Rummy, donde el objetivo es formar un trío de cartas del mismo valor.
```

# Descripción
```
Cada jugador recibe tres cartas de un mazo de 52 cartas. En su turno, puede robar una carta y descartar otra. Gana quien forme un trío primero.
```

# Pseudocódigo Inicial
```
Inicio
    Crear un mazo de 52 cartas y barajarlo
    Repartir tres cartas a cada jugador
    
    Repetir hasta que un jugador forme un trío:
        Si turno del jugador:
            Mostrar su mano
            Preguntar si desea robar del mazo o pila de descarte
            Descartar una carta
        
        Si turno de la máquina:
            Tomar decisiones según estrategia simple
        
        Verificar si un jugador ha formado un trío
    
    Si el jugador formó el trío primero
        Escribir "¡Ganaste el Rummy!"
    Sino
        Escribir "¡La máquina ha ganado el Rummy!"
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
        Imprimir "=== ESTAMOS JUGANDO RUMMY ==="
    FIN FUNCIÓN

    FUNCIÓN mostrar_reglas_rummy()
        Imprimir reglas del juego
    FIN FUNCIÓN

    FUNCIÓN repartir_mano()
        Definir valores de cartas ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        Crear mazo con 4 copias de cada valor (52 cartas)
        Mezclar el mazo de forma aleatoria
        Retornar una mano de 3 cartas (extraídas del mazo) y el mazo restante
    FIN FUNCIÓN

    FUNCIÓN verificar_ganador(mano)
        SI todas las cartas en la mano son iguales ENTONCES
            RETORNAR Verdadero
        SINO
            RETORNAR Falso
        FIN SI
    FIN FUNCIÓN

    FUNCIÓN jugar_rummy()
        Mostrar reglas del juego
        Repartir mano inicial al jugador y actualizar el mazo
        Repartir mano inicial a la máquina y actualizar el mazo
        Inicializar contador de manos en 0

        MIENTRAS Verdadero HACER
            Incrementar contador de manos
            Limpiar pantalla
            Mostrar título
            Mostrar número de mano actual
            Mostrar reglas del juego

            // Mostrar mano del jugador
            Imprimir "Tu mano: [mano del jugador]"

            // Verificar si el jugador ha ganado
            SI verificar_ganador(mano del jugador) ENTONCES
                Imprimir "¡Felicidades! Has ganado el Rummy."
                SALIR DEL BUCLE
            FIN SI

            // Solicitar acción al jugador
            Imprimir "Elige una opción: 1. Robar del mazo 2. Descartar una carta"
            INTENTAR
                Leer opción del jugador
                SI opción es 1 ENTONCES
                    Robar una carta del mazo
                    Imprimir "Robaste: [carta robada]"
                    Solicitar al jugador que indique qué carta desea descartar (por índice)
                    SI índice es válido ENTONCES
                        Reemplazar la carta descartada por la carta robada
                    SINO
                        Imprimir "Índice inválido."
                    FIN SI
                SINO
                    Imprimir "Opción inválida."
                FIN SI
            CAPTURAR ValueError
                Imprimir "Entrada inválida, ingresa un número válido."
            CAPTURAR KeyboardInterrupt
                Imprimir "Has abandonado la partida. ¡Perdiste!"
                SALIR DEL PROGRAMA
            FIN INTENTAR

            // Verificar si la máquina ha ganado
            SI verificar_ganador(mano de la máquina) ENTONCES
                Imprimir "La máquina ha ganado el Rummy. ¡Inténtalo de nuevo!"
                SALIR DEL BUCLE
            FIN SI
        FIN MIENTRAS
    FIN FUNCIÓN

    PROGRAMA PRINCIPAL
        INTENTAR
            Llamar a la función jugar_rummy()
        CAPTURAR KeyboardInterrupt
            Imprimir "Has abandonado la partida. ¡Perdiste!"
        FIN INTENTAR
    FIN PROGRAMA PRINCIPAL
FIN
```