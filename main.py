import random
import hangman_ASCII

###  WORD LIBRARY  ###
word_list = ["aardvark", "baboon", "camel"]

end_of_game = False
user_life_counter = 6

### GENERATE A RANDOM WORD ###
chosen_word = random.choice(word_list)
#### DEBUG ####
print(chosen_word)

### CREATE "_" PLACEHOLDERS FOR EACH LETTER IN chosen_word  ###
display = []
for letter in chosen_word:
    display.append("_")

while not end_of_game:
### ASK USER TO GUESS LETTER ###
    guess = input("\nPlease Guess a letter: ").lower()
    
### CHECK IF guess IS IN chosen_word ###
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(hangman_ASCII.stages[user_life_counter])

            
    if guess not in chosen_word:
        user_life_counter -= 1
        print(hangman_ASCII.stages[user_life_counter])
        if user_life_counter == 0: 
            print("You Lose!")
            break  
### PRINT UPDATED LETTER TRAY ###
    print(f"{' '.join(display)}")
    
        
### CHECK IF USER WON ###    
    if "_" not in display: 
        end_of_game = True
        print('\nYou Win!')
        
