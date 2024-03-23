alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if direction != "encode" and direction != "decode":
    print("Invalid input")
    exit()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":   
    encrypt(text, shift)
if direction == "decode":
    decrypt(text, shift) 

def encrypt(plain_text=text, shift_amount=shift):
    encoded_text = ""
    for char in plain_text:
        position = alphabet.index(char)
        new_position = position + shift_amount
        encoded_text += alphabet[new_position]
    print(f"The encoded text is {encoded_text}")
    
def decrypt(plain_text=text, shift_amount=shift):
    decoded_text = ""
    for char in plain_text: 
        position = alphabet.index(char)
        old_position = position - shift_amount
        decoded_text += alphabet[old_position]
    print(f"The decoded text is {decoded_text}")       
        


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 