import random

from src.utils import print_success, print_warning, print_failed

class Wordle:
    def __init__(self, file_path: str, word_length: int=5, limit: int=200):
        self.file_path = file_path
        self.word_length = word_length
        self.words = self.generate_words(file_path, word_length, limit)

    def generate_words(self, file_path, word_length, limit):
        #reading file
        word_freq = []
        with open(self.file_path, 'r') as f:
            for line in f:
                word, freq = line.strip().split(', ')
                word_freq.append((word, int(freq)))
        #filtering words
        word_freq = list(filter(lambda w_freq: len(w_freq[0]) == word_length, word_freq))

        #sorting words
        word_freq = sorted(word_freq, key=lambda w_freq: w_freq[1], reverse=True)

        #dropping frequency
        words = [w_freq[0] for w_freq in word_freq]

        #limiting words
        words = words[:limit]

        return words

    def check_letters(self, word, guess):
        for w_letter, g_letter in zip(word, guess.upper()):
            if w_letter == g_letter:
                print_success(f' {g_letter} ', end='')
                print(' ', end='')
            elif g_letter in word:
                print_warning(f' {g_letter} ', end='')
                print(' ', end='')
            else:
                print_failed(f' {g_letter} ', end='')
                print(' ', end='')
        print()

    def run(self, ):
        word = random.choice(self.words).upper()
        num_try = 6
        success = False

        while num_try:

            guess_word = input(f'Enter a {len(word)} word (or "q" to quit): ')
            if guess_word.lower() == 'q':
                break

            if len(guess_word) != len(word):
                print(f'Word should be of length {len(word)}')
                continue

            if not guess_word.lower() in self.words:
                print('Your guess is either not valid or not in the list')
                continue

            self.check_letters(word, guess_word)

            if guess_word.upper() == word:
                success = True
                print()
                print_success('Congratulations! You have guessed the word')
                break

            num_try -= 1

        if not success:
            print_failed(f'Game Over!',)
            print()
            print_success(f' The word was "{word}".')