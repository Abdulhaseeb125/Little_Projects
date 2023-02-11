Morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
              'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
              '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '---.', " ": "|"
              }


def Encode(text):
    Code = ''
    for letter in text:
        for key, value in Morse_code.items():
            if letter == key.lower():
                Code += f" {value}"
    print(f"Morse Code: {Code}")


def Decode(cipher):
    Code = ""
    code_list = cipher.split(' ')
    for code in code_list:
        for key, value in Morse_code.items():
            if code == value:
                Code += key
    print(Code)


print("In Coded text '|' will represent a space in text")
option = int(input("1- Encode \n2- Decode\nChoose Operation:"))
if option == 1:
    text = input("Enter Text:")
    Encode(text)
elif option == 2:
    cipher = input("Enter Code: ")
    Decode(cipher)
else:
    print("Invalid Command...")

