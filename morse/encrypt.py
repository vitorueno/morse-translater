from constants import MORSE_MAP


def encrypt(message):
    cipher = '' 
    for letter in message.upper(): 
        if letter != ' ': 
            cipher += MORSE_MAP[letter] + ' '
        else: 
            cipher += '  '
    return cipher 