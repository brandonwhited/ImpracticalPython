#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
chosen_letters = list(chosen_word)
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
User_Input = input("Guess a letter: ")
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_letters:
    if letter ==  User_Input:
        print("Right")
    else:
        print("False")
        