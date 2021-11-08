# ~~ -------------------------------------------------------- ~~ #
# ~~ -------------------------------------------------------- ~~ #
# ~~ -------- Programmer: AJ Cassell (@BrotatoBoi). --------- ~~ #
# ~~ --------------- Program Name: Morse-God. --------------- ~~ #
# ~~ -------------------- Version: 0.1.5. ------------------- ~~ #
# ~~ -------------- Last Updated: July/13/2021. ------------- ~~ #
# ~~ ----------- Revision Date: November/2/2021. ------------ ~~ #
# ~~ --- Description: This program is a Morse-to-English  --- ~~ #
# ~~ ------------- translation app made with python.  ------- ~~ #
# ~~ -------------------------------------------------------- ~~ #
# ~~ -------------------------------------------------------- ~~ #


# ~ Import Needed Modules ~ #
from os import (system, name)
from random import (choice,randint)
from time import sleep


# ~ Global Variables ~ #
MORSE_TABLE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '\'': '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}


# ~ Main Class ~ #
class Main:
        def __init__(self):
            """
                Initialize the class.

                Variables:
                    self.__version__ (str): The version of the program.
                    self.__author__ (str): The author of the program.
                    self.__name__ (str): The name of the program.
                    self._isRunning (bool): A boolean to determine if the program is running.

                Logic:
                    Create the variables then execute the main loop.
            """

            # ~ Variables ~ #
            self.__version__ = '0.1.5'
            self.__author__ = 'AJ Cassell'
            self.__name__ = 'Morse-God'

            self._isRunning = True

            # ~ Execute The Main Loop ~ #
            self.execute()

        # ~ Translate To Morse Code ~ #
        def char_to_morse(self):
            """
                Translate from characters to Morse Code.

                Variables:
                    userMessager (str): The user's message.

                Logic:
                    Get the user's message then print the Morse Code of each character.
                    Then wait for user input to continue.
            """

            # ~ Variables ~ #
            userMessage = input("\n\t>> ").upper()

            # ~ Logic ~ #
            for char in userMessage:
                print("\t" + MORSE_TABLE[char], end='')
                sleep(0.5)

            input("\n\t>> Press Enter to Continue.")

        
        # ~ Translate from Morse Code ~ #
        def morse_to_char(self):
            """
                Translate from Morse Code to characters.

                Variables:
                    morseMessage (str): The user's message in Morse Code.

                Logic:
                    Get the user's message then print the characters of each morse code.
                    Then wait for user input to continue.
            """

            # ~ Variables ~ #
            morseMessage = input("\n\t>> ").split()

            # ~ Logic ~ #
            for morse in morseMessage:
                for key, value in MORSE_TABLE.items():
                    if value == morse:
                        print("\t" + key, end='')
                        sleep(0.5)

            input("\n\t>> Press Enter to Continue.")


        # ~ Main Loop ~ #
        def execute(self):
            """
                Execute the main loop.

                Logic:
                    While the program is running, get the user's input and then
                    translate to or from Morse Code. If the user wants to quit,
                    then exit the program.
            """

            # ~ Main Loop ~ #
            while self._isRunning:
                system('clear' if name == 'posix' else 'cls')

                print("\t\t\tWelcome to Morse-God!\n\n"
                     +"\t>>2morse: Translate from characters to Morse-Code\n"
                     +"\t>>2char: Translate from character to Morse-Code")

                userInput = input("\n\t>> ").lower()

                if userInput == '2morse':
                    self.char_to_morse()
                elif userInput == '2char':
                    self.morse_to_char()
                elif userInput == 'quit':
                    self._isRunning = False
                else:
                    print("\n\t>> Invalid Input.\n")
                    sleep(1)

# ~ Check if it is the main file to run Main(). ~ #
if __name__ == '__main__':
    Main()
