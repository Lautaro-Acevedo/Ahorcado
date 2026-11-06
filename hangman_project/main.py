#!/usr/bin/env python3
from game import HangmanGame
import utils
palabra = utils.get_random_word()
letraPalabra = HangmanGame(palabra)
print("_______BIENVENIDO AL AHORCADO_________")
print(letraPalabra.display_progress())

while not letraPalabra.is_won() and not letraPalabra.is_lost():
    letra = input("Ingrese una letra: ")

    if len(letra) != 1:
        print("!!Ingresaste mas de una letra o dejaste el espacio vacio!!")
        continue

    if not letra.isalpha():
        print("El valor ingresado no es una letra")
        continue
    if letra not in letraPalabra.used_letters:
        if letraPalabra.process_guess(letra):
            print("!!Felicidades encontraste una letra!!")
        else:
            print("La letra no pertenece a la palabra ")
    else:
        print("Esa letra ya la ingresaste")
    
    progreso = letraPalabra.display_progress()
    print(progreso)

    print(f"Letras adivinadas: {letraPalabra.guessed_letters}")
    print(f"Intentos restantes: {letraPalabra.max_errors - letraPalabra.errors}")

if letraPalabra.is_won():
    print("¡Ganaste!")
else:
    print("Fin del juego")
    print(f"La palabra secreta era: {palabra}")
