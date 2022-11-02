import random

###  WORD LIBRARY  ###
word_list = ["aardvark", "baboon", "camel"]

end_of_game = False

### GENERATE A RANDOM WORD ###
chosen_word = random.choice(word_list)
#### DEBUG ####
print(chosen_word)

### CREATE '_" PLACEHOLDERS FOR EACH LETTER IN chosen_word  ###
display = []
for letter in chosen_word:
    display.append("_")

while not end_of_game:
    
### ASK USER TO GUESS LETTER ###
    guess = input("Please Guess a letter: ").lower()

### CHECK IF guess IS IN chosen_word ###
    for position in range(len(chosen_word)):
     letter = chosen_word[position]
     if letter == guess:
         display[position] = letter
         
    print(display)
    
    if "_" not in display: 
        end_of_game = True
        
print('You Win!')