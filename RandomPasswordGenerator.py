#!/usr/bin/python3

import random
import string

def generate_password(length):
# Get a random selection of letters, digits and puunctuation
    characters = string.ascii_letters + string.digits + string.punctuation
#shuffle the chracters to get a random selection
    characters = random.sample(characters, k=length)
# Join the charactesr into a single string and return it
    return "".join(characters)


#Generate a random password with a length of 12 cheacters

password = generate_password(13)
print(password) 
