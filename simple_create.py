import syllable_creation
import random

def syllable_preferences():
    #ask the user for an integer of max syllables per word and a mean syllables per word
    while True:
        try:
            max_syllables = int(input('Enter the maximum number of syllables per word: '))
            break
        except ValueError:
            print ('Please enter a number. \n')
    return max_syllables

def create_word(max_syllables):
    unjoined_word = []
    #generate a random integer between 1 and max_syllables
    syllable_target = random.randint(1, max_syllables)
    for i in range(syllable_target):
        syllable = syllable_creation.create_syllable()
        unjoined_word.append(syllable)
    word = ''.join(unjoined_word)
    return word

def simple_create():
    #ask the user how many words they would like to generate and require integer input
    while True:
        try:
            num_words = int(input('How many words would you like to generate? '))
            break
        except ValueError:
            print ('Please enter a number. \n')
    #ask about syllables
    max_syllables = syllable_preferences()
    #generate the requested number of words
    words = []
    for i in range(num_words):
        word = create_word(max_syllables)
        words.append(word)
    #print the generated words
    print ('\nGenerated words: ')
    print (words)
    #ask the user if they would like the words saved to a text file
    while True:
        save = input('Would you like to save these words to a text file? (y/n) ')
        if save == 'y':
            with open('output/generated_words.txt', 'w') as file:
                for word in words:
                    file.write(word + '\n')
            print ('Words saved to generated_words.txt. \n')
            break
        elif save == 'n':
            print ('Words not saved. \n')
            break
        else:
            print ('Invalid input. Please try again. \n')



