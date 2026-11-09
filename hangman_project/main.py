#!/usr/bin/env python3

# Definimos la lista con todos los estados del dibujo
AHORCADO_DIBUJOS = [
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",  # 0 fallos
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",  # 1 fallo
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",  # 2 fallos
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",  # 3 fallos
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",  # 4 fallos
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",  # 5 fallos
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="   # 6 fallos
]

from game import HangmanGame # importamos la clase HangmanGame
import utils # importamos el archivo utils

# Realizamos sus instancias
palabra = utils.get_random_word()  
letraPalabra = HangmanGame(palabra)

# Creamos una función para imprimir el dibujo en pantalla
def mostrar_ahorcado(errores):
    # Imprime el dibujo correspondiente al número de fallos (0 al 6)
    if 0 <= errores < len(AHORCADO_DIBUJOS):
        print(AHORCADO_DIBUJOS[errores])

print("_______BIENVENIDO AL AHORCADO_________")
mostrar_ahorcado(letraPalabra.errors)
print(letraPalabra.display_progress()) # imprimimos las celdas de la palabra a adivinar 

# No termina el juego hasta que el jugador gane o pierda
while not letraPalabra.is_won() and not letraPalabra.is_lost():
    letra = input("Ingrese una letra: ") # le pedimos una letra

    if len(letra) != 1: # validamos que sea solo 1
        print("!!Ingresaste mas de una letra o dejaste el espacio vacio!!")
        continue

    if not letra.isalpha(): # Validamos que sea una letra
        print("El valor ingresado no es una letra")
        continue

    # Validamos si ya ingreso esa letra
    if letra not in letraPalabra.used_letters:
        if letraPalabra.process_guess(letra): # Si pertenece a la palabra
            print("!!Felicidades encontraste una letra!!")
        else:
            print("La letra no pertenece a la palabra ")
    else:
        print("Esa letra ya la ingresaste")
    
    mostrar_ahorcado(letraPalabra.errors)
    progreso = letraPalabra.display_progress() # Devolvemos el progreso nuevamente de la palabra
    print(progreso)

    # Le mostramos las letras adivinadas y cuantos intentos le quedan
    print(f"Letras adivinadas: {letraPalabra.guessed_letters}")
    print(f"Intentos restantes: {letraPalabra.max_errors - letraPalabra.errors}")

# Si no gano, perdio 
if letraPalabra.is_won():
    print("¡Ganaste!")
else:
    print("Fin del juego")
    print(f"La palabra secreta era: {palabra}")
