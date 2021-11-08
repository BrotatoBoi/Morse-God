// Programmer: AJ Cassell (@BrotatoBoi).
// Program Name: Morse-God.
// Date: November/04/2021.
// Description: This is a C Plus Plus re-write of my Python Morse-God program.


// Define Variables.
#define __VERSION__ "0.1.5"
#define __DATE__ "November/04/2021"
#define __NAME__ "Morse-God"
#define __AUTHOR__ "AJ Cassell"


// Import Libraries.
#include <iostream>
#include <string>
#include <map>


// Use namespaces.
using std::cout; using std::cin; using std::endl;
using std::string; using std::map;


// Global Variables.
map<string, string> MORSE_TABLE = {
    {"A", ".-"}, {"B", "-..."}, {"C", "-.-."}, {"D", "-.."}, {"E", "."}, {"F", "..-."},
    {"G", "--."}, {"H", "...."},{"I", ".."}, {"J", ".---"}, {"K", "-.-"}, {"L", ".-.."},
    {"M", "--"}, {"N", "-."}, {"O", "---"}, {"P", ".--."}, {"Q", "--.-"}, {"R", ".-."},
    {"S", "..."}, {"T", "-"}, {"U", "..-"}, {"V", "...-"}, {"W", ".--"}, {"X", "-..-"},
    {"Y", "-.--"}, {"Z", "--.."}, {"0", "-----"}, {"1", ".----"}, {"2", "..---"},
    {"3", "...--"}, {"4", "....-"}, {"5", "....."}, {"6", "-...."}, {"7", "--..."},
    {"8", "---.."}, {"9", "----."}, {".", ".-.-.-"}, {",", "--..--"}, {"?", "..--.."},
    {"\'", ".----."}, {"!", "-.-.--"}, {"/", "-..-."}, {"(", "-.--."}, {")", "-.--.-"},
    {"&", ".-..."}, {":", "---..."}, {";", "-.-.-."}, {"=", "-...-"}, {"+", ".-.-."},
    {"-", "-....-"}, {"_", "..--.-"}, {"\"", ".-..-."}, {"$", "...-..-"}, {"@", ".--.-."},
    {" ", "/"}
};

// Translate Message to Morse.
string char_to_morse() {
    string message;
    string morse_message = "";

    cout << "Enter a message to translate to Morse >> ";
    cin >> message;
    
    for (int i=0; i<message.length(); i++) {
        if (MORSE_TABLE.find(message[i]) != MORSE_TABLE.end()) {
            morse_message += MORSE_TABLE[message[i]];
            morse_message += " ";
        }
    }

    return morse_message;
}


// Translate Morse to Message.
string morse_to_char() {
    string morse;
    string message = "";

    cout << "Enter Morse to translate to a message >> ";
    cin >> morse;

    for(int i=0; i<morse.length(); i++) {
        if(MORSE_TABLE.find(morse[i]) != MORSE_TABLE.end()) {
            message += MORSE_TABLE[morse[i]];
        }
    }

    return message;
}

// TO-DO: Make the damn app functional... I dislike C++...
// Main function.
int main() {
    // Create Variables.
    bool _isRunning = true;
    string welcome_message = "Welcome to " + string(__NAME__) + " V" + string(__VERSION__) + " By: " + string(__AUTHOR__) + ".";
    string userInput;

    while (_isRunning) {
        // Print the program name and version.

        cout << welcome_message << endl;
        cout << ">> 2morse: Translate message to morse." << endl << ">> 2char: Translate morse to message." << endl;

        // Get user input.
        cout << ">> ";
        cin >> userInput;

        // Check userInput.
        if(userInput == "2morse") {
            cout << char_to_morse() << endl;
        } else if(userInput == "2char") {
            cout << morse_to_char() << endl;
        } else if(userInput == "exit") {
            // Exit the program.
            _isRunning = false;
        } else {
            // Print error message.
            cout << "Error: Invalid command." << endl;
        }
    }
}
