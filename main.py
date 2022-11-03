import random
import hangman_ASCII
import words
from os import system, name

end_of_game = False
user_life_counter = 6
guess_bank = []

def clear():
    if name == 'nt':
        _ = system('cls')

print(hangman_ASCII.logo)
print(hangman_ASCII.stages[user_life_counter])

### GENERATE A RANDOM WORD ###
chosen_word = random.choice(words.list)
#### DEBUG ####
print(chosen_word)

### CREATE "_" PLACEHOLDERS FOR EACH LETTER IN chosen_word  ###
display = []
for letter in chosen_word:
    display.append("_")

print(f"{' '.join(display)}")

while not end_of_game:
    
### ASK USER TO GUESS LETTER ###
    guess = input("\nPlease Guess a letter: ").lower()
    clear()
    
    print(hangman_ASCII.logo)
    
    if guess in guess_bank:
        print(f"You have already guessed {guess}!")

### CHECK IF guess IS IN chosen_word ###
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(hangman_ASCII.stages[user_life_counter])
            guess_bank.append(guess)

    if guess not in chosen_word:
        user_life_counter -= 1
        print(hangman_ASCII.stages[user_life_counter])
        print(f"{guess} is not in this word.")
        guess_bank.append(guess)

        if user_life_counter == 0: 
            print(hangman_ASCII.lose)
            break  
### PRINT UPDATED LETTER TRAY ###
    print(f"{' '.join(display)}")
    
        
### CHECK IF USER WON ###    
    if "_" not in display: 
        end_of_game = True
        print(hangman_ASCII.win)
        
