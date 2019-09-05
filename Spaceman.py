import random

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def split(secret_word):
  return list(secret_word)
  print(split(word))

def get_guessed_word(secret_word, letters_guessed):
    blank_space = "_" * len(secret_word)
    print(blank_space)

def is_guess_in_word(guess, secret_word):

  if len(guess) != 1:
    print("You can only guess one letter per turn, try again!")
  elif guess in secret_word:
    print("That letter is in the secret word!")
  else:
    print("That letter is not in the secret word!")
    value[1] -= 1
  if value[1] == 0:
    print("You have lost the game, the word was: " + str(secret_word))
  guess1 = set(split(secret_word))
  if guess in guess1:
    str.replace(guess, blank_space)

def spaceman(secret_word):
    introduction = f"The word contains {value[0]} letters. You have a total of 7 turns per game. You only have {value[1]} before you lose. Try again!"
    print(introduction)

secret_word = load_word()
value = [len(secret_word), 7]
while value[1] is not 0:
    spaceman(secret_word)
    guess = input("Guess a letter: ")
    is_guess_in_word(guess, secret_word)
    get_guessed_word(secret_word, 0)
else:
  print("You have lost the game! The word was:" +str(secret_word))

