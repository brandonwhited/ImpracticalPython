alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if direction != "encode" and direction != "decode":
    print("Invalid input")
    exit()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
   
def caesar(text, shift, direction):
    cipher_text = ""
    for char in text:
        position = alphabet.index(char)
        if direction == "encode":
            new_position = position + shift
        elif direction == "decode":
            new_position = position - shift
        cipher_text += alphabet[new_position]
    print(f"The {direction}d text is {cipher_text}")



caesar(text, shift, direction)

input("Would you like to continue? Press Enter to exit.")
