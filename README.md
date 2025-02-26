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

## 🚀 Cómo Ejecutar los Juegos
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/nombre-del-repositorio.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd nombre-del-repositorio
   ```
3. Ejecuta cada juego con Python:
   ```bash
   python problema1_batalla_naval.py
   ```
   ```bash
   python problema2_triqui_memoria.py
   ```
   ```bash
   python problema3_sudoku.py
   ```
   ```bash
   python problema4_blackjack.py
   ```
   ```bash
   python problema5_rummy.py
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