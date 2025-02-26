# Proyecto: Juegos en Python 🎮

Este repositorio contiene el desarrollo del **Proyecto 1** de la asignatura **Programación (G02)**, correspondiente a la **Facultad de Ingeniería y Ciencias Básicas** en el **Programa Académico de Ingeniería de Datos e Inteligencia Artificial**.

## 📌 Objetivos
- Familiarizarse con las fases de desarrollo de software: **análisis, pseudocódigo, codificación, pruebas, depuración y documentación**.
- Aplicar el uso de **funciones, estructuras de decisión y repetitivas** en Python.

## 📋 Metodología
- El proyecto debe ser desarrollado en **grupos de 3 a 4 personas**.
- Para cada problema, los entregables son:
  1. **Análisis del problema**.
  2. **Algoritmo en pseudocódigo**.
  3. **Implementación funcional en Python**.
  4. **Evidencias de ejecución del programa** (capturas de pantalla).

## 📂 Entregables
- **📄 Informe en PDF (30%)**: Contiene análisis, pseudocódigo y capturas de pantalla.
- **💻 Código en Python (40%)**: Implementado en Jupyter Notebook y subido a GitHub.
- **🎤 Sustentación (30%)**: Se realizará el **jueves 06 de marzo de 2025** en horario de clase.

## 🕹️ Problemas a Resolver

### **Problema 1: Batalla Naval** 🚢
Diseñar e implementar una versión en Python del juego **Batalla Naval** con las siguientes reglas:
- Tablero de **5x5**, cada jugador tiene **3 barcos**.
- Se juega contra la **máquina** (la máquina coloca sus barcos aleatoriamente).
- El jugador **ingresa manualmente** la posición de sus barcos.
- La máquina **ataca aleatoriamente**, el jugador ingresa sus ataques.
- Se indica si el ataque es **acierto o fallo**.
- Gana quien **hunda los 3 barcos del oponente**.

=== ESTAMOS JUGANDO BATALLA NAVAL ===

  0 1 2 3 4
0 ❓ ❓ ❓ ❓ ❓
1 ❓ ❓ ❓ ❓ ❓
2 ❓ ❓ ❓ ❓ ❓
3 ❓ ❓ ❓ ❓ ❓
4 ❓ ❓ ❓ ❓ ❓

🃏 Número de intentos usados: 0

Ingresa la fila para atacar (0-4): 0
Ingresa la columna para atacar (0-4): 0
¡Impacto! Hundiste un barco enemigo.


### **Problema 2: Triqui y Juego de Memoria** ❌⭕🃏
El usuario puede elegir entre:
- **Triqui (Tic-Tac-Toe):**
  - Se escoge aleatoriamente quién empieza.
  - El usuario ingresa coordenadas para su jugada.
  - La máquina juega aleatoriamente.
  - Se indica el **ganador o si hay empate**.
- **Juego de Memoria:**
  - Tablero de **6x5** con **15 pares de figuras**.
  - Se destapan pares de cartas hasta formar coincidencias.
  - Gana quien **descubra más pares**.

### **Problema 3: Sudoku** 🔢
- Se almacenan **5 tableros de Sudoku** de nivel **fácil**.
- Se selecciona un tablero aleatoriamente.
- El usuario **ingresa números** y coordenadas para resolverlo.
- Se verifica si las jugadas son **correctas o incorrectas**.
- Al final, se indica si el usuario **ganó**.

### **Problema 4: Black Jack** 🃏
- Se juega con un **mazo estándar de 52 cartas**.
- Se escoge aleatoriamente quién empieza.
- Cada jugador puede **tomar una carta o plantarse**.
- Se juega con **50 créditos** y se apuesta hasta **10 créditos por ronda**.
- Gana quien alcance **100 créditos** primero.

### **Problema 5: Rummy** 🃏
- Se usa un **mazo de 52 cartas**.
- Se reparten **3 cartas** a cada jugador.
- Se deben formar **tríos** de cartas del mismo valor.
- Se puede **robar una carta** del mazo o la pila de descarte.
- Gana quien **forme un trío primero**.

## 📂 Estructura del Repositorio
```
/ │── README.md # Documentación del proyecto
│── informe.pdf # Documento con análisis, pseudocódigo y capturas
│── problema_1/
│ ├── batalla_naval.py # Código de Batalla Naval
│ ├── batalla_navalGUI.py # Interfaz gráfica (opcional)
│ └── pseudocodigo.md # Pseudocódigo del problema 1
│── problema_2/
│ ├── triqui_memoria.py # Código de Triqui y Juego de Memoria
│ └── pseudocodigo.md # Pseudocódigo del problema 2
│── problema_3/
│ ├── sudoku.py # Código de Sudoku
│ └── pseudocodigo.md # Pseudocódigo del problema 3
│── problema_4/
│ ├── blackjack.py # Código de Black Jack
│ └── pseudocodigo.md # Pseudocódigo del problema 4
│── problema_5/
├── rummy.py # Código de Rummy
└── pseudocodigo.md # Pseudocódigo del problema 5
```
======================================================================
## ==============================JUEGOS==============================
======================================================================
```
=== ESTAMOS JUGANDO BATALLA NAVAL ===

===== REGLAS DE BATALLA NAVAL =====
- Tablero de 5x5, cada jugador tiene 3 barcos.
- La máquina coloca sus barcos aleatoriamente.
- Tú debes ingresar las coordenadas de tus barcos.
- En cada turno, atacas una posición e intentas hundir los barcos enemigos.
- Gana quien hunda primero los 3 barcos del oponente.
===================================

  0 1 2 3 4
0
1
2
3
4

🃏 Número de intentos usados: 0

Ingresa la fila para atacar (0-4):
======================================================================

=== ESTAMOS JUGANDO TRIQUI ===

===== REGLAS DE TRIQUI =====
- Juego en un tablero de 3x3.
- Dos jugadores: Tú (X) vs Máquina (O).
- Gana quien complete una fila, columna o diagonal con su símbolo.
- Si el tablero se llena y no hay ganador, es un empate.
===================================

    0   1   2
  -------------
0 |   | ⭕ |   |
  -------------
1 |   |   |   |
  -------------
2 |   |   |   |
  -------------
Ingresa la fila (0-2):
```
======================================================================
```
======================
   🎴 JUEGO DE MEMORIA 🎴
======================

  0 1 2 3 4
0 ❓ ❓ ❓ ❓ ❓
1 ❓ ❓ ❓ 🥕 ❓
2 ❓ ❓ ❓ ❓ ❓
3 ❓ ❓ ❓ ❓ ❓
4 ❓ 🌽 ❓ ❓ ❓
5 ❓ ❓ ❓ ❓ ❓

🤖 La máquina falló. Se vuelven a tapar.
🃏 Número de intentos usados: 1

  0 1 2 3 4
0 ❓ ❓ ❓ ❓ ❓
1 ❓ ❓ ❓ ❓ ❓
2 ❓ ❓ ❓ ❓ ❓
3 ❓ ❓ ❓ ❓ ❓
4 ❓ ❓ ❓ ❓ ❓
5 ❓ ❓ ❓ ❓ ❓

Tu turno: Elige dos cartas para destapar.
Ingresa la fila de la primera carta (0-5): 0
Ingresa la columna de la primera carta (0-4): 0
Ingresa la fila de la segunda carta (0-5): 0
Ingresa la columna de la segunda carta (0-4): 1
```
======================================================================
```
=== ESTAMOS JUGANDO SUDOKU ===

===== REGLAS DE SUDOKU =====
- Se elige aleatoriamente un tablero de Sudoku 9x9 incompleto.
- Debes completar los espacios vacíos con números del 1 al 9.
- No puede haber números repetidos en filas ni columnas.
- Ganas si completas correctamente el tablero.
===================================

    0   1   2   3   4   5   6   7   8
  ------------------------------------
0 |   | 5 | 1 | 4 | 6 |   | 4 | 9 | 5 |
  ------------------------------------
1 |   |   | 1 | 9 | 8 |   |   |   | 6 |
  ------------------------------------
2 |   | 2 |   |   | 1 |   |   |   |   |
  ------------------------------------
3 |   |   | 2 | 9 | 7 |   | 5 | 9 |   |
  ------------------------------------
4 |   |   |   | 3 | 6 |   |   | 6 |   |
  ------------------------------------
5 |   | 3 | 2 |   | 9 | 8 | 3 |   | 7 |
  ------------------------------------
6 | 7 | 3 | 5 |   |   | 6 |   | 4 | 6 |
  ------------------------------------
7 | 7 | 7 | 7 | 8 |   |   | 1 |   |   |
  ------------------------------------
8 | 9 | 9 | 5 | 5 |   |   |   |   | 7 |
  ------------------------------------
Ingresa la fila (0-8):
```
======================================================================
```
=== ESTAMOS JUGANDO BLACK JACK ===

=== RONDA #1 ===
Rondas jugadas: 0

=========================== REGLAS DE BLACK JACK ===========================
- Se juega con un mazo estándar de 52 cartas.
- El objetivo es llegar a 21 puntos o lo más cerca posible sin pasarse.
- Cada jugador empieza con 50 créditos y apuesta hasta 10 créditos por ronda.
- Gana quien llegue primero a 100 créditos.
- Historial de Rondas: G (Ganada) y P (Perdida).
===============================================================================

=== JUGUEMOS ===
Tienes Créditos 50.
¿Cuántos créditos deseas apostar? (Máximo 10)
Ingresa tu apuesta: 10
Tu mano: ['7', 'K'], Puntaje: 17
¿Deseas otra carta? (s/n):
```
======================================================================
```
=== ESTAMOS JUGANDO RUMMY ===

=== MANO #1 ===

===== REGLAS DE RUMMY =====
- Se usa un mazo estándar de 52 cartas.
- Cada jugador recibe 3 cartas al inicio.
- En cada turno, puedes robar una carta y descartar una.
- Gana quien forme un trío de cartas del mismo valor primero.
===================================


Tu mano: ['2', '9', '9']
Elige una opción: 1. Robar del mazo 2. Descartar una carta
Opción:
```
======================================================================

## 🚀 Cómo Ejecutar los Juegos
1. Clona este repositorio:
   ```bash
   git clone https://github.com/driosoft-pro/programming_Projec-1.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd programming_Projec-1
   ```
3. Ejecuta cada juego con Python:
   ```bash
   python batalla_naval.py
   ```
   ```bash
   python triqui.py
   python memoria.py
   ```
   ```bash
   python sudoku.py
   ```
   ```bash
   python blackjack.py
   ```
   ```bash
   python rummy.py
   ```

## 🛠 Requisitos
- Python 3.x
- No se requiere instalación de librerías adicionales

## 📜 Licencia
Este proyecto está bajo la licencia MIT - Puedes usarlo libremente. 😊

---
¡Esperamos que disfrutes estos juegos en Python! 🚀

## Autor
📌 **By:** Deyton Riascos Ortiz