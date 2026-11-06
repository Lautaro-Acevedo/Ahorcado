#!/usr/bin/env python3

#clase Hangmangame
class HangmanGame:
    #inicializacion de constructor
    def __init__(self, word):
        self.word = word.lower() # nuestra palabra a adivinar
        self.guessed_letters = [] # letras adivinas por el jugador
        self.used_letters = [] # letras insertadas por el jugador
        self.max_errors = 6 # cantidad maxima de intentos
        self.errors = 0 # Cuantas veces se equivoca
    
    #Retornamos el progreso de la palabra
    def display_progress(self):
        progress = ""
        #Recorremos la palabra letra por letra y validamos
        for letra in self.word:
            if letra == " ":
                progress += "   "
            elif not letra.isalpha(): # Si no es una letra la muestra
                progress += letra + " "
            elif letra in self.guessed_letters: # Si ya la adivino la muestra
                progress += letra + " "
            else:
                progress += "_ "

        return progress # Retornamos la palabras con las letras adivinados

    # Validamos si la letra pertenece a la palabra
    def process_guess(self, letra):
        letra = letra.lower() 
        if letra in self.word: # Validamos si pertenece a la palabra
            if letra not in self.guessed_letters:
                # Si no pertenece se agrega a las encontradas y ingresadas
                self.guessed_letters.append(letra)
                self.used_letters.append(letra)
            return True
        else:
            # Si no pertenece a la palabra se le suma una oportunidad menos
            self.used_letters.append(letra)
            self.errors += 1
            return False
    
    # Validamos si ya adivino la palabra
    def is_won(self):
        for letra in self.word:
            if letra.isalpha() and letra not in self.guessed_letters:
                return False # Faltan letras por adivinar      
        return True  # Ya adivino todas las letras                    

    # Validamos si ya llego al limite de intentos
    def is_lost(self):
        if self.errors >= self.max_errors:
            return True # perdio
        else:
            return False # sigue en juego