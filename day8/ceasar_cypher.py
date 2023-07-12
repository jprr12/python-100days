# # ceasar cipher 1 - encryption
import os
import ceasar_art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(code_word, shift_num):
#     cipher_text =''
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"
#     for char in code_word:
#         if shift_num <= 26:
#             position = alphabet.index(char)
#             new_position = position + shift_num
#             if new_position > 25:
#                 new_position -= 26
#             new_char = alphabet[new_position]
#             cipher_text += new_char
#         elif shift_num > 26:
#             print("Cannot encrypt. Shift number should be less than 26.")
#             break
    
#     print(f"The encoded text is: {cipher_text}")

# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(encrypted_txt, shift_num):
#     #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#     #e.g. 
#     #cipher_text = "mjqqt"
#     #shift = 5
#     #plain_text = "hello"
#     #print output: "The decoded text is hello"
#     decrypted_txt = ''
#     for char in encrypted_txt:
#         position = alphabet.index(char)
#         new_position = position - shift_num
#         # if new_position < 0:
#         #     new_position += 26
#         new_char = alphabet[new_position]
#         decrypted_txt += new_char
#     print(f"The decrypted word is {decrypted_txt}")

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
# text = input("Type your message: ").lower()
# shift = int(input("Type the shift number: "))

# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# if direction.lower() == 'encode':
#     encrypt(text, shift)
# elif direction.lower() == 'decode':
#     decrypt(text, shift)
# else:
#     print("Wrong input.")

# code reorganization
# combine the encrypt() and decrypt() functions into one called ceasar()
def ceasar(code_word, shift_num, direction):
    encrypted_txt = ''
    if direction == 'decode':
        shift_num *= -1
    for char in code_word:
        # if non-alphabet is inputed
        if char not in alphabet:
            encrypted_txt += char
            continue
        position = alphabet.index(char)
        new_position = position + shift_num
        # if user input > 25
        if new_position > 25:
            encrypted_txt += alphabet[new_position % 26]
        else:
            encrypted_txt += alphabet[new_position]
    print(f"The {direction}d text is: {encrypted_txt}")
# user prompt function
def menu():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    # function call
    ceasar(text, shift, direction)

print(ceasar_art.logo)
again = True
while again == True:
    menu()
    try_again = input("Wanna try again? yes or no: ")
    if try_again.lower() == 'yes':
        os.system('cls')
        continue
    elif try_again.lower() == 'no':
        break

# improving UX
# added visuals, etc.


