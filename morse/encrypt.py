from .constants import MORSE_MAP


def encrypt(message):
    cipher = ''
    for char in message.upper():
        if char == ' ':
            cipher += '  '  # two spaces
        else:
            cipher += f'{MORSE_MAP[char]} '
    return cipher