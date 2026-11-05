#!/usr/bin/env python3
from game import HangmanGame
import utils
palabra = utils.get_random_word()
letraPalabra = HangmanGame(palabra)
print("_______BIENVENIDO AL AHORCADO_________")
print(letraPalabra.display_progress())

while True:
    letra = input("Ingrese una letra: ")

    if len(letra) != 1:
        print("!!Ingresaste mas de una letra o dejaste el espacio vacio!!")
        continue

    if not letra.isalpha():
        print("El valor ingresado no es una letra")
        continue

    if letraPalabra.process_guess(letra):
        print("!!Felicidades encontraste una letra!!")
    else:
        print("La letra no pertenece a la palabra ")

    progreso = letraPalabra.display_progress()
    print(progreso)
    print(f"Errores: {letraPalabra.errors}/{letraPalabra.max_errors}")

    if "_" not in progreso:
        print("Ganaste")
        break
    
    if letraPalabra.errors >= letraPalabra.max_errors:
        print("Fin del juego")
        print(f"La palabra secreta era: {palabra}")
        break
