import random
import string


class Hangman:
    # Default 6 wrong guesses - Head, torso, arms, legs
    max_wrong_guesses = 6
    guessed_letters = []
    curWord = ''
    wrongGuesses = 0

    def __init__(self, max_guess=6):
        self.max_wrong_guesses = max_guess

    # Pulls a random word from the word list
    def new_word(self):
        word = random.choice(list(open('words.txt'))).rstrip()
        self.curWord = word
        return word

    # Checks if user has exhausted wrong answers
    def has_guesses(self, num):
        if num <= self.max_wrong_guesses:
            return True
        else:
            return False

    # Checks if word has been guessed
    def guessed_word(self):
        return set(self.curWord) <= set(self.guessed_letters)

    # Returns full word with underscores
    def printWord(self):
        result = ''
        for char in self.curWord:
            if char in self.guessed_letters:
                result += ' {} '.format(char)
            else:
                result += '_ '
        return result

    def checkLetter(self, letter):
        if len(letter) == 1 and letter in string.ascii_letters:
            if letter in self.guessed_letters:
                return "You've already guessed {}, try again! ".format(letter)
            else:
                self.guessed_letters.append(letter)
                if letter in self.curWord:
                    return 'Letter {} found'.format(letter)
                else:
                    msg = "Letter {} not found! You have {} guesses remaining.".format(letter,
                                                                                       self.max_wrong_guesses - self.wrongGuesses)
                    self.wrongGuesses += 1
                    return msg
        else:
            return "Try again, but this time with ONE letter."

    def reset(self):
        self.wrongGuesses = 0
        self.guessed_letters = []
        self.curWord = self.new_word()
