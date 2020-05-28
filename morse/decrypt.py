from .constants import MORSE_MAP


def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for char in message:
        if char != ' ':
            i = 0
            citext += char
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_MAP.keys())[list(MORSE_MAP
                                                        .values()).index(citext)]
                citext = ''
    return decipher
