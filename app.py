# Import Modules
import string
import time
from random import *

# Utility Variables
minumumChars = 10
maximumChars = 15

# Core Functions
def generateCode(generatedCode):
    stringChars = string.ascii_letters + string.punctuation + string.digits
    generatedCode = "".join(choice(stringChars) for x in range(randint(minumumChars, maximumChars)))
    print(f"Successfully encrypted your text! Please use the code {generatedCode} to decrypt your text")
    return generatedCode


def Program():
    print("Encryption/Decryption Program")
    time.sleep(1)
    
    while True:
        chosenCommand = input("Commands: Encrypt, Decrypt: ")

        if chosenCommand.lower() == 'encrypt':
            encryptedText = input("Please type in the text you would like to encrypt: ")
            generatedCode = generateCode(encryptedText)
    
        elif chosenCommand.lower() == 'decrypt':
            decryptCode = input("Please paste the code to decrypt your text: ")

            if decryptCode == generatedCode:
                print(f"Your text is {encryptedText}")
            elif decryptCode != generatedCode:
                print("Incorrect Code!")
            else:
                print("An error occured!")
        else:
            print(f'Critical Error: Command "{chosenCommand}" does not exist!')

Program()
