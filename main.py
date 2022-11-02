import random

###  WORD LIBRARY  ###
word_list = ["aardvark", "baboon", "camel"]

### GENERATE A RANDOM WORD ###
chosen_word = random.choice(word_list)

### ASK USER TO GUESS LETTER ###
guess = input("Please Guess a letter: ").lower()

### CHECK IF guess IS IN chose_word ###
for letter in chosen_word:
    if letter == guess:
        print('Right')
    else:
        print('Wrong')