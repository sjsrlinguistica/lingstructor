import json

def check_phonemes():
    #check for the existence of phonemes.json
    phonemes_file = 'cache/phonemes.json'
    phonemes_defined = False
    print ('PHONEMES:')
    try:
        with open(phonemes_file, "r") as file:
            phonemes = json.load(file)
            print('Vowels: ' + str(phonemes["vowels"]))
            print('Consonants: ' + str(phonemes["consonants"]) + '\n')
            phonemes_defined = True
    except FileNotFoundError:
        print ('No phonemes are currently defined. \n')
        #append phoneme_file to a program_state.json file 
        phonemes_defined = False
    return phonemes_defined

def check_syllable():
    #check for the existence of syllable_structure.json
    syllable_file = 'cache/syllable_structure.json'
    print ('SYLLABLE STRUCTURE:')
    try:
        with open(syllable_file, "r"):
            #read the content of the file and print it
            with open('cache/syllable_structure.json', 'r') as file:
                syllable_structure = json.load(file)
                print(''.join(syllable_structure) + '\n')
    except FileNotFoundError:
        print ('No syllable structure is currently defined. \n')

def status_check():
    #introduce the function
    print ('Checking the current state of the program... \n')
    while True:
        check_phonemes()
        check_syllable()
        break #if a function returns false, stop the function