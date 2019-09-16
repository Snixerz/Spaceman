import random
letters_guessed = []

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    word = []
    for letter in secret_word:
        if letter in letters_guessed:
            word.append(letter)
    return secret_word == word

def get_guessed_word(secret_word, letters_guessed):
    word = []
    for letter in secret_word:
        if letter in letters_guessed:
            word.append(letter)
        else:
            word.append('_')
    return ''.join(word)

def is_guess_in_word(guess, secret_word):
    if guess in secret_word:
        return True
    else:
        return False

def spaceman(secret_word):
    print("Welcome! Let's play Spaceman! You get a lotal of 7 guesses.")
    guesses = value[1]
    while  True:
        guess = input('Guess a letter: ')
        letters_guessed.append(guess)

        if is_guess_in_word(guess, secret_word) is False:
            print(get_guessed_word(secret_word,letters_guessed))
            guesses -= 1
            print(f'Incorrect! You have {guesses} turn(s) remaining')
        elif is_guess_in_word(guess, secret_word) is True:
          print("Correct, guess another letter!")

        if len(guess) > 1 or len(guess) == 0:
            print('Only single letters. Try again!')

        if guesses == 0:
          print(f'You lost the game. The secret word was {secret_word}')
          break
        
        is_guess_in_word(guess, secret_word)

    get_guessed_word(secret_word,letters_guessed)

secret_word = load_word()
value = (len(secret_word), 7)
spaceman(secret_word)