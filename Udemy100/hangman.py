#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
chosen_letters = list(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
for _ in chosen_letters:
    display.append("_")
# OR display += "_"
# OR display = ["_" for _ in chosen_letters]
# OR for _ in range(len()chosen_word): display += "_"

#TODO-2: - Loop through each position in the chosen_word;

guess = input("Guess a letter: ").lower()

for i, letter in enumerate(chosen_letters):
    if letter == guess:
        display[i] = guess
        
# OR for position in range(len(chosen_word)):
#       letter = chosen_word[position]
#       if letter == guess:
#           display[position] = letter


print(display)