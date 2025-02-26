# Problema 4: Black Jack 🃏
```
Diseñe e implemente una versión del juego Black Jack en Python utilizando un mazo estándar de 52 cartas.
```

# Descripción
```
Dos jugadores compiten en Black Jack. Cada jugador puede tomar cartas o plantarse en su turno. Se apuesta hasta 10 créditos por ronda. Gana quien llegue a 100 créditos primero.
```

# Pseudocódigo Inical
```
Inicio
    Crear un mazo de 52 cartas y barajarlo
    Asignar 50 créditos a cada jugador
    
    Repetir hasta que un jugador alcance 100 créditos:
        Repartir cartas iniciales a los jugadores
        
        Repetir hasta que ambos jugadores se planten:
            Si turno del jugador:
                Preguntar si quiere tomar carta o plantarse
                Si toma carta, agregarla a su mano
            Si turno de la máquina:
                Tomar decisiones según estrategia simple
        
        Evaluar ganador de la ronda y ajustar créditos
    
    Si el jugador alcanza 100 créditos
        Escribir "¡Ganaste el Black Jack!"
    Sino
        Escribir "¡La máquina ha ganado el Black Jack!"
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
        Imprimir "=== ESTAMOS JUGANDO BLACK JACK ==="
    FIN FUNCIÓN

    FUNCIÓN mostrar_reglas_blackjack()
        Imprimir reglas del juego
    FIN FUNCIÓN

    FUNCIÓN obtener_valor_carta(carta)
        SI carta es "J", "Q" o "K" ENTONCES
            RETORNAR 10
        SINO SI carta es "A" ENTONCES
            RETORNAR 11
        SINO
            RETORNAR convertir carta a entero
        FIN SI
    FIN FUNCIÓN

    FUNCIÓN repartir_carta()
        Definir cartas posibles ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        RETORNAR una carta seleccionada al azar
    FIN FUNCIÓN

    FUNCIÓN calcular_puntaje(mano)
        Calcular total como la suma de los valores de las cartas en la mano
        SI hay un "A" en la mano y total > 21 ENTONCES
            Restar 10 al total
        FIN SI
        RETORNAR total
    FIN FUNCIÓN

    FUNCIÓN jugar_blackjack()
        Mostrar reglas del juego
        Inicializar créditos del jugador y la máquina en 50
        Inicializar número de ronda en 0
        Inicializar lista de historial de rondas vacía

        MIENTRAS créditos del jugador < 100 Y créditos de la máquina < 100 HACER
            Incrementar número de ronda
            Limpiar pantalla
            Mostrar título
            Mostrar número de ronda y rondas jugadas
            SI hay historial de rondas ENTONCES
                Mostrar historial de rondas
            FIN SI
            Mostrar reglas del juego

            // Obtener apuesta válida del jugador
            MIENTRAS apuesta < 1 O apuesta > 10 O apuesta > créditos del jugador HACER
                Mostrar créditos del jugador
                Solicitar apuesta al jugador
                SI apuesta es inválida ENTONCES
                    Mostrar mensaje de error
                FIN SI
            FIN MIENTRAS

            // Repartir cartas al jugador y a la máquina
            Repartir dos cartas al jugador
            Repartir dos cartas a la máquina
            Mostrar mano y puntaje del jugador

            // Permitir al jugador tomar más cartas
            MIENTRAS puntaje del jugador < 21 HACER
                Solicitar al jugador si desea otra carta
                SI el jugador elige tomar otra carta ENTONCES
                    Repartir una carta al jugador
                    Mostrar mano y puntaje del jugador
                SINO
                    SALIR DEL BUCLE
                FIN SI
            FIN MIENTRAS

            // La máquina toma cartas hasta alcanzar al menos 17 puntos
            MIENTRAS puntaje de la máquina < 17 HACER
                Repartir una carta a la máquina
            FIN MIENTRAS

            // Mostrar mano y puntaje de la máquina
            Mostrar mano y puntaje de la máquina

            // Determinar el resultado de la ronda
            SI puntaje del jugador > 21 ENTONCES
                El jugador pierde la ronda
                Restar apuesta a los créditos del jugador
                Sumar apuesta a los créditos de la máquina
                Agregar "P" al historial de rondas
            SINO SI puntaje de la máquina > 21 O puntaje del jugador > puntaje de la máquina ENTONCES
                El jugador gana la ronda
                Sumar apuesta a los créditos del jugador
                Restar apuesta a los créditos de la máquina
                Agregar "G" al historial de rondas
            SINO
                La máquina gana la ronda
                Restar apuesta a los créditos del jugador
                Sumar apuesta a los créditos de la máquina
                Agregar "P" al historial de rondas
            FIN SI

            // Mostrar resumen de la ronda
            Mostrar resumen de la ronda (resultado, créditos del jugador y máquina)

            // Verificar si alguien alcanzó 100 créditos
            SI créditos del jugador >= 100 O créditos de la máquina >= 100 ENTONCES
                SALIR DEL BUCLE
            FIN SI

            // Preguntar si desea continuar jugando
            Solicitar al jugador si desea continuar jugando
            SI el jugador elige no continuar ENTONCES
                SALIR DEL BUCLE
            FIN SI
        FIN MIENTRAS

        // Mostrar resumen final del juego
        Mostrar total de rondas jugadas
        Mostrar rondas ganadas y perdidas
        SI créditos del jugador >= 100 ENTONCES
            Mostrar "¡Felicidades! Has ganado el Black Jack."
        SINO SI créditos de la máquina >= 100 ENTONCES
            Mostrar "La máquina ha ganado el Black Jack. ¡Inténtalo de nuevo!"
        SINO
            SI créditos del jugador > créditos de la máquina ENTONCES
                Mostrar "Has abandonado el juego, pero tenías más créditos. ¡Técnicamente ganaste!"
            SINO SI créditos de la máquina > créditos del jugador ENTONCES
                Mostrar "Has abandonado el juego y la máquina tenía más créditos. ¡Has perdido!"
            SINO
                Mostrar "Has abandonado el juego con un empate en créditos."
            FIN SI
        FIN SI
    FIN FUNCIÓN

    PROGRAMA PRINCIPAL
        INTENTAR
            Llamar a la función jugar_blackjack()
        CAPTURAR KeyboardInterrupt
            Mostrar "Has abandonado la partida. ¡Perdiste!"
        FIN INTENTAR
    FIN PROGRAMA PRINCIPAL
FIN
```