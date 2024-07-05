
#imports
import status_check
import phoneme_functions
import syllable_functions
import simple_create
import generate_lexicon
import json
import time
import os

# Get the current working directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script's directory
os.chdir(current_directory)

def main():
    print ('\nLingstructor v0.1 \n')
    print ('This program can help you generate words or a lexicon for your conlang. \n')
    time.sleep(1) #wait 1 second
    #function to display the current state of the program
    status_check.status_check()
    #if pass
    #else pass:
    #print a list of 3 choices
    #ask user to select a choice
    while True:
        print ('\nMAIN MENU\n1. Phonology\n2. Syllable Structure\n3. Generation Functions\n4. Exit\n')
        user_input = input('Please select a choice (1-4): ')
        response = user_input.strip().lower()
        if response == '1':
            phoneme_functions.edit_phonemes()
        elif response == '2':
            syllable_functions.request_syllable()
        elif response == '3':
            #ask the user if they would like to generate a set number of words, or if they would like to generate a lexicon
            print ('\nGENERATION FUNCTIONS\n1. Generate Words\n2. Generate Lexicon\n3. Return to Main Menu\n')
            user_input = input('Please select a choice (1-3): ')
            response = user_input.strip().lower()
            if response == '1':
                simple_create.simple_create()
            elif response == '2':
                generate_lexicon.generate_lexicon()
            elif response == '3':
                continue
        elif response == '4':
            print('Exiting...')
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

#program can only run as stand-alone
if __name__ == "__main__":
    main()