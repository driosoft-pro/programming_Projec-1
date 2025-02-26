import random  # Importa la librería random para operaciones aleatorias
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
    print("=== === === === === ESTAMOS JUGANDO RUMMY === === === === ===")

# ======================= RUMMY =======================
# Funciones y lógica para el juego de Rummy

def mostrar_reglas_rummy():
    # Imprime las reglas del juego en pantalla
    print("\n===================== REGLAS DE RUMMY =====================")
    print("- Se usa un mazo estándar de 52 cartas.")
    print("- Cada jugador recibe 3 cartas al inicio.")
    print("- En cada turno, puedes robar una carta y descartar una.")
    print("- Gana quien forme un trío de cartas del mismo valor primero.")
    print("==============================================================\n")

def repartir_mano():
    # Define los valores de las cartas y construye un mazo completo (4 de cada valor)
    valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    mazo = valores * 4  # Crea un mazo de 52 cartas (4 cartas de cada valor)
    random.shuffle(mazo)  # Mezcla el mazo de forma aleatoria
    # Retorna una mano de 3 cartas (extraídas del mazo) y el mazo restante
    return [mazo.pop() for _ in range(3)], mazo

def verificar_ganador(mano):
    # Verifica si todas las cartas en la mano son iguales, lo que indica que se forma un trío
    return all(carta == mano[0] for carta in mano)

def jugar_rummy():
    # Función principal para ejecutar el juego de Rummy
    mostrar_reglas_rummy()  # Muestra las reglas al jugador
    mano_jugador, mazo = repartir_mano()  # Reparte la mano del jugador y actualiza el mazo
    mano_maquina, mazo = repartir_mano()  # Reparte la mano de la máquina y actualiza el mazo
    
    num_manos = 0  # Contador de manos jugadas

    while True:
        num_manos += 1  # Incrementamos el contador de manos
        limpiar_pantalla()  # Limpia la pantalla antes de cada turno
        mostrar_titulo()  # Muestra el título del juego
        print(f"\n=== MANO #{num_manos} ===")
        mostrar_reglas_rummy()  # Muestra las reglas al jugador

        # Muestra en pantalla la mano actual del jugador
        print(f"\nTu mano: {mano_jugador}")
        # Si el jugador tiene un trío, se declara ganador y termina el juego
        if verificar_ganador(mano_jugador):
            print("\n¡Felicidades! Has ganado el Rummy.")
            break
        
        # Solicita al jugador que elija su acción: robar o descartar
        print("Elige una opción: 1. Robar del mazo 2. Descartar una carta")
        try:
            opcion = int(input("Opción: "))  # Lee la opción elegida
            if opcion == 1:
                # Si el jugador opta por robar, se saca la última carta del mazo
                carta_robada = mazo.pop()
                print(f"Robaste: {carta_robada}")
                # Se le pide al jugador que indique qué carta desea descartar (por índice)
                print("¿Cuál carta deseas descartar? (Ingresa el índice 0, 1 o 2)")
                descarte = int(input("Índice: "))
                if descarte in [0, 1, 2]:
                    # Reemplaza la carta descartada por la carta robada
                    mano_jugador[descarte] = carta_robada
                else:
                    print("Índice inválido.")
            else:
                # Si la opción no es 1, se informa que es inválida
                print("Opción inválida.")
        except ValueError:
            # Captura el error en caso de que la entrada no sea numérica
            print("Entrada inválida, ingresa un número válido.")
        except KeyboardInterrupt:
            # Captura el cierre abrupto del juego
            print("\nHas abandonado la partida. ¡Perdiste!")
            exit()  # Sale del programa
        
        # Verifica si la mano de la máquina es ganadora, en cuyo caso la máquina gana
        if verificar_ganador(mano_maquina):
            print("\nLa máquina ha ganado el Rummy. ¡Inténtalo de nuevo!")
            break

# Programa principal: se ejecuta cuando se corre el script directamente.
if __name__ == "__main__":
    try:
        jugar_rummy()
    except KeyboardInterrupt:
        print("\nHas abandonado la partida. ¡Perdiste!")