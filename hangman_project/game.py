#!/usr/bin/env python3


class HangmanGame:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        progress = ""

        for letra in self.word:
            if not letra.isalpha():
                progress += letra + " "
            elif letra in self.guessed_letters:
                progress += letra + " "
            else:
                progress += "_ "

        return progress

    def process_guess(self, letra):
        if letra in self.word:
            if letra not in self.guessed_letters:
                self.guessed_letters.append(letra)
            return True
        else:
            self.errors += 1
            return False