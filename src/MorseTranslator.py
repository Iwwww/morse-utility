# Python program to implement Morse Code Translator

'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''


import re

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {# English
                   'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',

                   # Russian
                   'А': '-.', 'Б': '-...', 'В': '.--',
                    'Г': '--.', 'Д': '-..', 'Е': '.',
                    'Ж': '...-', 'З': '--..', 'И': '..',
                    'Й': '.---', 'К': '-.-', 'Л': '.-..',
                    'М': '--', 'Н': '-.', 'О': '---',
                    'П': '.--.', 'Р': '.-.', 'С': '...',
                    'Т': '-', 'У': '..-', 'Ф': '..-.',
                    'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
                    'Ш': '----', 'Щ': '--.-', 'Ь': '-..-',
                    'Ъ': '-..-', 'Ы': '-.--', 'Э': '..-..',
                    'Ю': '..--', 'Я': '.-.-',

                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----',

                   ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-',
                   ':': '---...', ';': '-.-.-.',
                   '"': '.-..-.',

                   ' ':'/'
                   }

def getAlphobet(sing=None):
    if sing == None:
        return MORSE_CODE_DICT

    else:
        return MORSE_CODE_DICT[sing]



# Function to encrypt the string
# according to the morse code chart
def encrypt(message, MORSE_CODE_DICT=MORSE_CODE_DICT):
    cipher = ''
    for letter in message:
        if letter not in MORSE_CODE_DICT:
            print(letter, "no in dict")

        elif letter == ' ':
            cipher = cipher + " / "

        else:

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '


    return cipher


# Function to decrypt the string
# from morse to english
def decrypt(message, MORSE_CODE_DICT=MORSE_CODE_DICT):
    output_letter = ''

    for letter in re.split(r" ", message):
        if letter == '/':
            output_letter += ' '
        else:
            try:
                output_letter += get_key(MORSE_CODE_DICT, letter)
            except:
                pass

    return output_letter


def get_key(dict, value):
    for key, v in dict.items():
        if v == value:
            return key


# Executes the main function
if __name__ == '__main__':
    print(get_key(MORSE_CODE_DICT, '.....'))
    message = str(input("TEXT: "))
    result = encrypt(message.upper())

    print(result)

    message = str(input("MORSE: "))
    result = decrypt(message)
    print(result)

