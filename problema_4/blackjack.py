import random  # Importa la librería random para generar números aleatorios
import os  # Importa el módulo os para limpiar la pantalla

# Función para limpiar la pantalla de la consola.
def limpiar_pantalla():
    # Verifica el sistema operativo y ejecuta el comando correspondiente.
    if os.name == "nt":  # Para Windows.
        os.system("cls")
    else:  # Para macOS y Linux.
        os.system("clear")

# Función para mostrar el título del juego.
def mostrar_titulo():
    print("=== ESTAMOS JUGANDO BLACK JACK ===")

# ======================= BLACK JACK =======================
# Define las funciones y lógica para jugar Blackjack

def mostrar_reglas_blackjack():
    # Imprime en pantalla las reglas del juego
    print("\n=========================== REGLAS DE BLACK JACK ===========================")
    print("- Se juega con un mazo estándar de 52 cartas.")
    print("- El objetivo es llegar a 21 puntos o lo más cerca posible sin pasarse.")
    print("- Cada jugador empieza con 50 créditos y apuesta hasta 10 créditos por ronda.")
    print("- Gana quien llegue primero a 100 créditos.")
    print("- Historial de Rondas: G (Ganada) y P (Perdida).")
    print("===============================================================================\n")

def obtener_valor_carta(carta):
    # Retorna el valor numérico de la carta
    # Las cartas J, Q y K valen 10
    if carta in ["J", "Q", "K"]:
        return 10
    # El as (A) vale 11 de manera predeterminada
    elif carta == "A":
        return 11
    # Para el resto de cartas, convierte el string a entero
    else:
        return int(carta)

def repartir_carta():
    # Define las cartas posibles de un mazo y retorna una seleccionada al azar
    cartas = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    return random.choice(cartas)

def calcular_puntaje(mano):
    # Calcula el puntaje total de una mano de cartas
    total = sum(obtener_valor_carta(carta) for carta in mano)
    # Ajusta el valor del as (A) si el total supera 21
    if "A" in mano and total > 21:
        total -= 10
    return total

# Función para llevar registro de las rondas
def jugar_blackjack():
    # Función principal para jugar Blackjack
    mostrar_reglas_blackjack()  # Muestra las reglas al inicio
    jugador_creditos, maquina_creditos = 50, 50  # Inicializa los créditos de jugador y máquina
    
    # Variables para llevar registro de las rondas
    num_ronda = 0
    historial_rondas = []  # Lista para guardar resultados: "G" (ganada) o "P" (perdida)
    
    # Continúa con el juego hasta que alguno alcance 100 créditos o el usuario decida salir
    while jugador_creditos < 100 and maquina_creditos < 100:
        num_ronda += 1  # Incrementamos el número de ronda
        limpiar_pantalla()  # Limpia la pantalla antes de cada ronda
        mostrar_titulo()  # Muestra el título del juego
        
        # Mostramos información de las rondas
        print(f"\n=== RONDA #{num_ronda} ===")
        print(f"Rondas jugadas: {num_ronda-1}")
        
        # Mostramos historial de rondas si hay alguna jugada
        if historial_rondas:
            historial = " ".join([f"{i+1}:{resultado}" for i, resultado in enumerate(historial_rondas)])
            print(f"Historial de rondas: {historial}")
        
        mostrar_reglas_blackjack()  # Muestra las reglas al jugador
        
        # Bucle para obtener una apuesta válida
        apuesta = 0
        while apuesta < 1 or apuesta > 10 or apuesta > jugador_creditos:
            print(f"=== JUGUEMOS ===")
            print(f"Tienes Créditos {jugador_creditos}.")
            print(f"¿Cuántos créditos deseas apostar? (Máximo 10)")
            try:
                apuesta = int(input("Ingresa tu apuesta: "))  # Solicita la apuesta del jugador
                    
                # Valida que la apuesta esté dentro de los límites permitidos
                if apuesta < 1:
                    print("La apuesta debe ser al menos 1 crédito. Inténtalo de nuevo.")
                elif apuesta > 10:
                    print("La apuesta máxima permitida es de 10 créditos. Inténtalo de nuevo.")
                elif apuesta > jugador_creditos:
                    print(f"No tienes suficientes créditos. Solo tienes {jugador_creditos} créditos disponibles.")
                
            except ValueError:
                print("Entrada inválida. Ingresa un número válido.")
                continue  # Vuelve al inicio en caso de error de conversión
            except KeyboardInterrupt:
                print("\nHas abandonado la partida. ¡Perdiste!")
                exit()  # Sale del programa si el usuario cancela
        
        # Reparte dos cartas para el jugador y para la máquina
        mano_jugador = [repartir_carta(), repartir_carta()]
        mano_maquina = [repartir_carta(), repartir_carta()]
        
        # Muestra la mano y el puntaje actual del jugador
        print(f"Tu mano: {mano_jugador}, Puntaje: {calcular_puntaje(mano_jugador)}")
        
        # Permite al jugador tomar cartas mientras no se pase de 21
        while calcular_puntaje(mano_jugador) < 21:
            try:
                opcion = input("¿Deseas otra carta? (s/n): ").lower()
                if opcion == "s":
                    mano_jugador.append(repartir_carta())
                    print(f"Tu mano: {mano_jugador}, Puntaje: {calcular_puntaje(mano_jugador)}")
                else:
                    break  # Sale del bucle si el jugador decide detenerse
            except KeyboardInterrupt:
                print("\nHas abandonado la partida. ¡Perdiste!")
                exit()  # Sale del programa si el usuario cancela
        
        # La máquina toma cartas hasta alcanzar un puntaje de al menos 17
        while calcular_puntaje(mano_maquina) < 17:  
            mano_maquina.append(repartir_carta())
        
        # Muestra la mano y el puntaje final de la máquina
        print(f"Mano de la máquina: {mano_maquina}, Puntaje: {calcular_puntaje(mano_maquina)}")
        
        # Condiciones para determinar el ganador de la ronda:
        if calcular_puntaje(mano_jugador) > 21:
            # Si el jugador se pasa de 21, pierde la ronda
            print("Te pasaste de 21. Pierdes la ronda.")
            jugador_creditos -= apuesta
            maquina_creditos += apuesta
            historial_rondas.append("P")  # Registramos como ronda perdida
        elif calcular_puntaje(mano_maquina) > 21 or calcular_puntaje(mano_jugador) > calcular_puntaje(mano_maquina):
            # Gana el jugador si la máquina se pasa de 21 o si su puntaje es mayor
            print("¡Ganaste la ronda!")
            jugador_creditos += apuesta
            maquina_creditos -= apuesta
            historial_rondas.append("G")  # Registramos como ronda ganada
        else:
            # En cualquier otro caso, gana la máquina la ronda
            print("La máquina gana esta ronda.")
            jugador_creditos -= apuesta
            maquina_creditos += apuesta
            historial_rondas.append("P")  # Registramos como ronda perdida
        
        # Mostramos resumen de la ronda
        print(f"\n=== RESUMEN RONDA #{num_ronda} ===")
        print(f"Resultado: {'Ganada' if historial_rondas[-1] == 'G' else 'Perdida'}")
        print(f"Tus créditos: {jugador_creditos}")
        print(f"Créditos máquina: {maquina_creditos}")
        
        # Verificamos si alguno alcanzó 100 créditos
        if jugador_creditos >= 100 or maquina_creditos >= 100:
            break
        
        # Preguntamos si desea continuar jugando
        while True:
            try:
                continuar = input("\n¿Deseas continuar jugando? (s/n): ").lower()
                if continuar in ["s", "n"]:
                    break
                else:
                    print("Por favor, ingresa 's' para continuar o 'n' para salir.")
            except KeyboardInterrupt:
                print("\nHas abandonado la partida. ¡Perdiste!")
                exit()
        
        if continuar == "n":
            print("\nHas decidido terminar el juego.")
            break
    
    # Al salir del bucle, se determina el ganador final según los créditos obtenidos
    print(f"\n=== RESUMEN FINAL ===")
    print(f"Total de rondas jugadas: {num_ronda}")
    ganadas = historial_rondas.count("G")
    perdidas = historial_rondas.count("P")
    print(f"Rondas ganadas: {ganadas}")
    print(f"Rondas perdidas: {perdidas}")
    
    if jugador_creditos >= 100:
        print("\n¡Felicidades! Has ganado el Black Jack.")
    elif maquina_creditos >= 100:
        print("\nLa máquina ha ganado el Black Jack. ¡Inténtalo de nuevo!")
    else:
        # Si el usuario decidió salir antes de que alguien llegue a 100 créditos
        if jugador_creditos > maquina_creditos:
            print("\nHas abandonado el juego, pero tenías más créditos. ¡Técnicamente ganaste!")
        elif maquina_creditos > jugador_creditos:
            print("\nHas abandonado el juego y la máquina tenía más créditos. ¡Has perdido!")
        else:
            print("\nHas abandonado el juego con un empate en créditos.")
            
# Programa principal: se ejecuta cuando se corre el script directamente
if __name__ == "__main__":
    try:
        jugar_blackjack()
    except KeyboardInterrupt:
        print("\nHas abandonado la partida. ¡Perdiste!")