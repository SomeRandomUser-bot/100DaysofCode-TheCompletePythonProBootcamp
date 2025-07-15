# import art
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
#
# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#
#     for letter in original_text:
#         if encode_or_decode == "decode":
#             shift_amount *= -1
#
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]
#     print(f"Here is the {encode_or_decode}d result: {output_text}")
#
#
# print(art.logo)
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
#
# caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ' ']

alphabet.extend(numbers)
alphabet.extend(symbols)
finished = False
restart = ""

import art

def caesar(original_text, shift_amount, encode_decode_choice):
    cyphertext = ""
    if encode_decode_choice == "encode":
        for letter in original_text:
            shiftletter = alphabet.index(letter) + shift_amount
            shiftletter %= len(alphabet) # Using Modulo will grants us to always stay in 0-25 range
            cyphertext += alphabet[shiftletter]
        print(cyphertext)
    else:
        for letter in original_text:
            shiftletter = alphabet.index(letter) - shift_amount
            shiftletter %= len(alphabet) # Using Modulo will grants us to always stay in 0-25 range
            cyphertext += alphabet[shiftletter]
        print(cyphertext)

print(art.logo)
while not finished:
    restart = ""
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
    else:
        print("Wrong answerer, please try again")
    while restart != "yes" and restart != "no":
        restart = input("Do you want to continue? Yes/No\n").lower()
        if restart == "yes":
            finished = False
        elif restart == "no":
            finished = True
            print("Goodbye!")
        else:
            print("Wrong answer, please try again.")