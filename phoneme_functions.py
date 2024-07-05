import json
import numpy as np 
import random

def request_phonemes(): #function to request user input on phonemes
    phonemes = list() #declare a list to store the phonemes
    phoneme_input=input('Please input your desired phonemes. \n') #get the user's input
    for char in phoneme_input: #parse the user's input and append it to the list of phonemes
        if char == ' ':
            pass
        elif char in phonemes:
            pass
        else:
            phonemes.append(char)
    return (phonemes)

def clean_phonemes(phonemes):
    #declare a list to store the phonemes
    ipa_phonemes = list() 

    #declare vowels and consonants
    ipa_cons = ['m', 'ɱ', 'p', 'b', 'n', 't', 'd', 'θ', 'ð', 's', 'z', 'ɹ', 'r', 'ɾ', 'l', 't', 'd', 'ʃ', 'ʒ', 'ɳ', 'ʈ', 'ɖ', 'ʂ', 'ʐ', 'ɻ', 'ɽ', 'ɽ', 'ɭ', 'ɲ', 'c', 'ɟ', 'ç', 'ʝ', 'j', 'ɢ̆', 'ŋ', 'k', 'g', 'x', 'ɣ', 'ɰ', 'ɴ', 'q', 'ɢ', 'χ', 'ʁ', 'ʡ', 'ħ', 'ʕ', 'ʔ', 'h', 'ɦ']
    ipa_vwls = ['i', 'y', 'ɨ', 'ʉ', 'ɯ', 'u', 'ɪ', 'ʏ', 'ʊ', 'e', 'ø', 'ɘ', 'ɵ', 'ɤ', 'o', 'e̞', 'ø̞', 'ə', 'ɤ̞', 'o̞', 'ɛ', 'œ', 'ɜ', 'ɞ', 'ʌ', 'ɔ', 'æ', 'ɐ', 'a', 'ɶ', 'ä', 'ɑ', 'ɒ']

    #clear [ɡ] doubles
    clean_g = 'ɡ'
    unicode_g = 'g'
    if clean_g in phonemes:    
        if unicode_g in phonemes:
            phonemes.remove(clean_g)
        else:
            for i in range(len(phonemes)):
                if phonemes[i] == clean_g:
                    phonemes[i] = unicode_g

    #prep output list
    phoneme_output = []

    #clear non-ipa
    ipa = ipa_cons + ipa_vwls
    for char in phonemes: # Check if the character is an IPA consonant
        if char in ipa: # If it is, add it to the output list
            phoneme_output.append(char)

    #create vowel and cons list
    vowel_phonemes = []
    cons_phonemes = []
    for char in phonemes:
        if char in ipa_vwls:
            vowel_phonemes.append(char)
        elif char in ipa_cons:
            cons_phonemes.append(char)

    phoneme_dict = {
        "all_phonemes": phoneme_output,
        "vowels": vowel_phonemes,
        "consonants": cons_phonemes
    }

    #write all the phonemes to a file
    with open('cache/phonemes.json', 'w') as json_outfile:
        json.dump(phoneme_dict, json_outfile, indent=1, separators=(',', ':'))

    #print the result of this script for the user
    num_vowels = str(len(vowel_phonemes))
    num_cons = str(len(cons_phonemes))

    print ('Your selected phonemes are:\n' + str(phoneme_dict['all_phonemes']) + '\n' + num_vowels + ' vowels\n' + num_cons + ' consonants')

def generate_vowel_num():
    #introduce this section)
    print ('Natural languages typically have between 2 and 15 vowel phonemes (SOURCE, YEAR)')
    print ('Please input the desired number of vowels for your language. If you are unsure, type "r" for a random number. \n')
    while True:
        num_vowels = input('Number of vowels: ')
        if num_vowels.isdigit():
            print ('Your language will have ' + str(num_vowels) + ' vowels.')
            return int(num_vowels)
        elif num_vowels == 'r':
            # Given probabilities (weights)
            system_weights = [1/315, 19/315, 25/315, 109/315, 60/315, 44/315, 19/315, 24/315, 8/315, 4/315, 2/315, 1/315, 1/315, 1/315]
            system_choices = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            # Pick one category based on the probabilities
            chosen_system_index = random.choices(range(len(system_weights)), weights=system_weights)[0]
            num_vowels = system_choices[chosen_system_index]
            print ('Your language will have ' + str(num_vowels) + ' vowels.')
            return int(num_vowels)
        else:
            print("Invalid input, please try again.")
            continue

def generate_vowels(num_vowels):
    all_vowels = ['i', 'y', 'ɨ', 'ʉ', 'ɯ', 'u', 'ɪ', 'ʏ', 'ʊ', 'e', 'ø', 'ɘ', 'ɵ', 'ɤ', 'o', 'e̞', 'ø̞', 'ə', 'ɤ̞', 'o̞', 'ɛ', 'œ', 'ɜ', 'ɞ', 'ʌ', 'ɔ', 'æ', 'ɐ', 'a', 'ɶ', 'ä', 'ɑ', 'ɒ']

    while True:
        if num_vowels == 2:
            vowels = ['e', 'o'] #placeholder
        elif num_vowels == 3:
            system_weights = [14/19, 3/19, 1/19, 1/19]
            system_choices = ['standard', 'holed', 'skewed', 'centralized']
            chosen_system_index = random.choices(range(len(system_weights)), weights=system_weights)[0]
            selected_system = system_choices[chosen_system_index]
            print ('Your language will have a ' + selected_system + ' ' + str(num_vowels) +' vowel system.')
            #declare the correct vowels
            if selected_system == 'standard':
                vowels = ['i', 'a', 'u'] #most common 3-vowel system
            elif selected_system == 'holed':
                roll = random.choice(['front', 'back'])
                if roll == 'front': #lowered front vowel
                    vowels = ['e', 'a', 'u']
                else: #lowered back vowel
                    vowels = ['i', 'a', 'o']
            elif selected_system == 'skewed':
                #flip a coin
                roll = random.choice(['lower', 'left'])
                if roll == 'lower': #lower skew
                    vowels = ['e', 'a', 'o']
                else: #left skew
                    vowels = ['i', 'e̩', 'a'] #second most common three vowel system
            else: #system is centralized
                vowels = ['i', 'ə', 'u'] 
        elif num_vowels == 4:
            vowels = ['i', 'e', 'a', 'u'] #placeholder
        elif num_vowels == 5:
            system_weights = [95/109, 14/109]
            system_choices = ['standard', 'nonstandard']
            chosen_system_index = random.choices(range(len(system_weights)), weights=system_weights)[0]
            selected_system = system_choices[chosen_system_index]
            print ('Your language will have a ' + selected_system + ' ' + str(num_vowels) +' vowel system.')
            if selected_system == 'standard':
                vowels = ['i', 'e', 'a', 'o', 'u'] #most common 5-vowel system
            else: #placeholder for nonstandard
                vowels = random.choices(all_vowels, k=5)
        elif num_vowels == 7:
            system_weights = [23/44, 21/44]
            system_choices = ['standard', 'nonstandard']
            chosen_system_index = random.choices(range(len(system_weights)), weights=system_weights)[0]
            selected_system = system_choices[chosen_system_index]
            print ('Your language will have a ' + selected_system + ' ' + str(num_vowels) +' vowel system.')
            if selected_system == 'standard':
                vowels = ['i', 'e', 'ɛ', 'a', 'o', 'ɔ','u'] #most common 7-vowel system
            else: #placeholder for nonstandard
                vowels = random.choices(all_vowels, k=7)
        
        print (vowels)

        #create a way to break the loop
        user_input = input("\nIs this vowel system acceptable (y/n): ").lower() # Ask the user if they want to continue
        if user_input == 'y':
            return vowels # Return the vowels
            break  # Break out of the loop
        else:
            print("\nRe-generating...")
            continue # Continue the loop

def generate_consonant_num():
    #introduce this section)
    print ('Natural languages typically have between 6 and 34 consonant phonemes (Maddieson, 2013)')
    print ('Please input the desired number of consonants for your language. If you are unsure, type "r" for a random number. \n')
    while True:
        num_cons = input('Number of consonants: ')
        if num_cons.isdigit() == True:
            print ('Your language will have ' + str(num_cons) + ' consonants.')
            return int(num_cons)
        elif num_cons == 'r':
            #generate a random number between 6 and 34 from a normal distribution with a mean of 22.7 and a std. dev 3.
            mean = 22.7
            std_dev = 3
            num_cons = int(max(6, min(34, np.random.normal(loc=mean, scale=std_dev))))
            print ('Your language will have ' + str(num_cons) + ' consonants.')
            return num_cons
        else:
            print("Invalid input, please try again.")

def generate_consonants(): 
    pass

def create_phonemes_main():
    print ('VOWEL DEVELOPMENT:')
    num_vowels = generate_vowel_num()
    vowels = generate_vowels(num_vowels)
    print ('\nCONSONANT DEVELOPMENT:')
    num_consonants = generate_consonant_num()
    print (num_consonants)
    #consonants = generate_consonants()

def sort_consonants():
    #open and read phonemes.json
    with open ('cache/phonemes.json') as p:
        phonemes = json.load(p)
    #sort the phonemes
    vowels = phonemes['vowels']
    consonants = phonemes['consonants']
    #declare consonant manners
    ipa_stops = ['p', 'b', 't', 'd', 'ʈ', 'ɖ', 'c', 'ɟ', 'k', 'g', 'q', 'ɢ', 'ʡ', 'ʔ']
    ipa_nasals = ['m', 'ɱ', 'n', 'ɳ', 'ɲ', 'ŋ', 'ɴ']
    ipa_taps = [ 'ⱱ', 'ɾ', 'ɽ']
    ipa_trills = ['ʙ', 'r', 'ʀ', 'ʜ', 'ʢ']
    ipa_fricatives = ['ɸ', 'β', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ', 'ʂ', 'ʐ', 'ç', 'ʝ', 'x', 'ɣ', 'χ', 'ʁ', 'ħ', 'ʕ', 'h', 'ɦ']
    ipa_lateralfricatives = ['ɬ', 'ɮ']
    ipa_apprixmants = ['ʋ', 'ɹ','ɻ','j','ɰ', 'ʍ', 'w']
    ipa_lateralapproiximants = ['l', 'ɭ', 'ʎ', 'ʟ']

    #declare lists to store consonant manners
    stops = []
    fricatives = []
    nasals = []
    liquids = []
    glides = []
    #sort consonants by manner of articulation
    for char in consonants:
        if char in ipa_stops:
            stops.append(char)
        elif char in ipa_fricatives:
            fricatives.append(char)
        elif char in ipa_nasals:
            nasals.append(char)
        else:
            print ('A consonant in your phonemes is not classifiable.')
            pass

    #declare consonant places
    ipa_bilabials = ['p', 'b', 'ɸ', 'β', 'm']
    ipa_labiodentals = ['f', 'v', 'ɱ', 'ⱱ','ʋ']
    ipa_dentals = ['θ', 'ð']
    ipa_alveolars = ['t', 'd', 'n', 'r', 'ɾ', 's', 'z', 'ɹ', 'ɬ', 'ɮ', 'l']
    ipa_postalveolars = ['ʃ', 'ʒ']
    ipa_retroflex = ['ʈ', 'ɖ', 'ɳ', 'ɽ', 'ʂ', 'ʐ', 'ɻ', 'ɭ']
    ipa_palatals = ['c', 'ɟ', 'ɲ', 'ç', 'ʝ', 'j', 'ʎ']
    ipa_velars = ['k', 'g', 'ŋ', 'x', 'ɣ', 'ɰ', 'ʟ']
    ipa_uvulars = ['q', 'ɢ', 'ɴ', 'ʀ', 'χ', 'ʁ']
    ipa_pharyngeals = ['ħ', 'ʕ']
    ipa_glottals = ['ʔ', 'h', 'ɦ']
    #declare lists to store consonant places
    bilabials = []
    labiodentals = []
    dentals = []
    alveolars = []
    postalveolars = []
    palatals = []
    velars = []
    uvulars = []
    glottals = []
    #sort consonants by place of articulation
    for char in consonants:
        if char in ipa_bilabials:
            bilabials.append(char)
        elif char in ipa_labiodentals:
            labiodentals.append(char)
        elif char in ipa_dentals:
            dentals.append(char)
        elif char in ipa_alveolars:
            alveolars.append(char)
        elif char in ipa_postalveolars:
            postalveolars.append(char)
        elif char in ipa_palatals:
            palatals.append(char)
        elif char in ipa_velars:
            velars.append(char)
        elif char in ipa_uvulars:
            uvulars.append(char)
        elif char in ipa_glottals:
            glottals.append(char)
        else:
            print ('A consonant in your phonemes is not classifiable.')
            pass
    #write the sorted consonants to a file
    with open('cache/sorted_consonants.json', 'w') as file:
        json.dump({'stops': stops, 'fricatives': fricatives, 'nasals': nasals, 'liquids': liquids, 'glides': glides, 'bilabials': bilabials, 'labiodentals': labiodentals, 'dentals': dentals, 'alveolars': alveolars, 'postalveolars': postalveolars, 'palatals': palatals, 'velars': velars, 'uvulars': uvulars, 'glottals': glottals}, file, indent=1, separators=(',', ':'))
    
    print('Vowels: ' + str(vowels))
    print('Consonants: ' + str(consonants)) 

def edit_phonemes(): #function to parse, clean, and export phonemes to a .json
    #ask useser if they want to import phonemes or autogen phonemes
    user_input = input('Do you already have phonemes in IPA?: \n(a) Yes! \n(b) No, help me create them!\n')
    while True:
        response = user_input.strip().lower()
        if response == 'a':
            phonemes=request_phonemes() #store returned phonemes as a variable
            clean_phonemes(phonemes)
            return True
        elif response == 'b':
            create_phonemes_main()
            return True
        else:
            print("Invalid input. Please enter choice 'a' or 'b'.")