#!/usr/bin/env python3
import random

def get_random_word():
    palabras = []
    with open("wordlist.txt", encoding="utf-8") as file:
        for line in file:
            p = line.strip()
            if p.isalpha():
                palabras = palabras + [p]
    return random.choice(palabras)
