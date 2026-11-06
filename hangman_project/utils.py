#!/usr/bin/env python3
import random # importamos la libreria random para utilizar una funcion

# Nos devolvera una palabra random
def get_random_word():
    palabras = []
    with open("wordlist.txt", encoding="utf-8") as file: # le nuestro archivo con palabras
        for line in file: # lo recorre
            p = line.strip() # eliminamos espacio o tabulaciones de mas
            if p:
                palabras = palabras + [p] # Agregamos todas las palabras a un arreglo
    return random.choice(palabras) # selecciona una random
