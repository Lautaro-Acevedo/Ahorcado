
# Juego del Ahorcado en Python

## Descripción del proyecto

Este proyecto consiste en desarrollar el juego del ahorcado utilizando Python, ejecutado desde la consola. El programa selecciona aleatoriamente el título de una película desde un archivo de texto y el jugador debe adivinar las letras que componen el título antes de alcanzar el límite de seis errores.

## Estructura del proyecto

```text
Ahorcado/
└── hangman_project/
    ├── main.py
    ├── game.py
    ├── utils.py
    ├── wordlist.txt
    └── README.md
```

## Descripción de los archivos

### main.py

Es el archivo principal del programa y se encarga de iniciar la partida, solicitar y validar las letras ingresadas, mostrar el progreso y representar las distintas etapas del dibujo del ahorcado.

### game.py

Contiene la clase `HangmanGame`, encargada de gestionar el estado y las reglas del juego.

### utils.py

Contiene la función `get_random_word()`, que lee el archivo `wordlist.txt` y selecciona una palabra aleatoriamente utilizando el módulo `random`.

### wordlist.txt

Contiene los títulos de películas disponibles para jugar, con una entrada por línea.

## Requisitos

- Python 3.
- Terminal de comandos.


## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Lautaro-Acevedo/Ahorcado.git
```

### 2. Ingresar a la carpeta del proyecto

```bash
cd Ahorcado/hangman_project
```

### 3. Ejecutar el juego

```bash
python3 main.py
```

## Reglas del juego

1. El programa selecciona aleatoriamente el título de una película.
2. El jugador debe ingresar una letra por turno.
3. Si la letra pertenece al título, se revelan sus posiciones.
4. Si la letra es incorrecta, se incrementa el contador de errores.
5. Después de cada intento, se actualiza el dibujo del ahorcado.
6. El jugador gana cuando descubre todas las letras.
7. El jugador pierde cuando alcanza seis errores.

