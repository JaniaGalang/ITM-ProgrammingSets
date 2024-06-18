'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    if letter == " ":
        return " "
    orig_position = ord(letter) - ord('A')
    new_position = (orig_position + shift) % 26
    new_letter = chr(new_position + ord('A'))
    return new_letter

def caesar_cipher(message, shift):
    def shift_letter(letter, shift):
        if letter==" ":
            return " "
        orig_position = ord(letter) - ord('A')
        new_position = (orig_position + shift) % 26
        new_letter = chr(new_position + ord('A'))
        return new_letter

    shifted_message = ""
    for letter in message:
        shifted_message += shift_letter(letter, shift)
    return shifted_message

def shift_by_letter(letter, letter_shift):

    if letter == " ":
        return " "
    orig_position = ord(letter) - ord('A')
    shift = ord(letter_shift) - ord('A')
    new_position = (orig_position + shift) % 26
    new_letter = chr(new_position + ord('A'))
    return new_letter

def vigenere_cipher(message, key):
    def shift_by_letter(letter, letter_shift):
        if letter == " ":
            return " "
        orig_position = ord(letter) - ord('A')
        shift = ord(letter_shift) - ord('A')
        new_position = (orig_position + shift) % 26
        new_letter = chr(new_position + ord('A'))
        return new_letter

    extended_key = (key * ((len(message)//len(key))+1))[:len(message)]
    
    encrypted_message = []

    key_index = 0
    for letter in message:
        if letter == " ":
            encrypted_message.append(letter)
            key_index += 1
        else:
            encrypted_message.append(shift_by_letter(letter, extended_key[key_index]))
            key_index += 1

    return "".join(encrypted_message)


def scytale_cipher(message, shift):

    orig_length = len(message)
    if orig_length % shift != 0:
        phrase_length = shift - (orig_length % shift)
        message += "_" * phrase_length
    phrase_length = len(message)
    encoded_message = [""] * phrase_length
    for i in range(phrase_length):
        encoded_index = (i // shift) + (phrase_length // shift) * (i % shift)
        encoded_message[i] = message[encoded_index]
    return "".join(encoded_message)

def scytale_decipher(message, shift):
    
    length = len(message)
    decoded_message = [""] * length
    for i in range(length):
        original_index = (i % shift) * (length // shift) + (i // shift)
        decoded_message[original_index] = message[i]
    return "".join(decoded_message)