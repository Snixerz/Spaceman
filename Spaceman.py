import random


def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)

    return secret_word


def get_guessed_word(secret_word, letters_guessed):
    blank_space = ""
    combine = ""
    for letter in secret_word:
        blank_space += "_"
    for x in temp_2:
        combine += x

    print(combine)


def is_guess_in_word(guess, secret_word):
    index = 0
    result = True
    for x in secret_word:
        if(guess == x):
            temp_2[index] = x
        else:
            result = False
        index += 1
    if result is False:
        value[1] -= 1

    pass


def spaceman(secret_word):
    introduction = f"""The word contains {value[0]} letters.
You have a total of 7 turns per game.
You only have {value[1]} before you lose. Try again!"""

    print(introduction)


secret_word = load_word()
value = [len(secret_word), 7]
temp_2 = []

for x in range(value[0]):
    temp_2.append("_")

while value[1] != 0:
    print("\033[H\033[J")
    get_guessed_word(secret_word, 0)
    spaceman(secret_word)
    guess = input("Guess a letter: ")
    is_guess_in_word(guess, secret_word)

print("You have lost the game! The word was: " + str(secret_word) + ".")
