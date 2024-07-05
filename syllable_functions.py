#local imports
import json
import random
 
def request_syllable():
    user_syllable_structure = [] #declare a string to store the syllable structure
    #request user input on syllable structure
    while True: #require user to provide valid input
        syllable_input=input('Please input your desired syllable structure using only the characters "C" and "V". \n') #get the user's input
        for char in syllable_input: #parse the user's input and append it to the list of phonemes
            if char in ['c', 'C', 'v', 'V']:
                user_syllable_structure.append(char)
            else:
                print ('Invalid input. Please try again.')
                break
        else: #if the user input is valid, break the loop
            break 
    #request the user to input if onsets are mandatory
    if 'c' or 'C'  in onset_input:
        while True: #require user to provide valid input
            onset_input=input('You have inputted that onsets are permissible. Would you like to make onsets mandatory? ')  
            if onset_input.lower == 'y': 
                mandatory_onset =  True
                break
            else:
                mandatory_onset = False
                break
        else:
            print ('Invalid input. Please try again.')
            Continue
    #make all syllable structures uppercase
    syllable_structure = [element.upper() for element in user_syllable_structure]
    #write the syllable structure to the structure cache
    with open('cache/syllable_structure.json', 'w') as file:
        json.dump(syllable_structure, file)
    #write the onset parameter to a the parameters cache
    with open('cache/syllable_parameters.json', 'w') as file2:
        json.dump(mandatory_onset, file2)

def generate_syllable_structure():
    #declare all possible parameters
    simple_onset = bool() #declare a boolean to store the simple onset
    complex_onset = bool() #declare a boolean to store the complex onset
    supercomplex_onset = bool() #declare a boolean to store the hypercomplex onset
    hypercomplex_onset = bool() #declare a boolean to store the superhypercomplex onset 
    simple_coda = bool() #declare a boolean to store the coda
    complex_coda = bool() #declare a boolean to store the complex coda
    supercomplex_coda = bool() #declare a boolean to store the hypercomplex coda
    hypercomplex_coda = bool() #declare a boolean to store the superhypercomplex coda
    mandatory_onset = bool() #declare a boolean to store the mandatory onset parameter
    #declare a list of possible syllable structures
    syllable_types = ["CCCV", "VC", "CVC", "CCVC", "CCCVC", "VCC", "CVCC", "CCVCC", "CCCVCC", "VCCC", "CVCCC", "CCVCCC", "CCCVCCC"]
    superclasses = ["simple", "moderately_complex", "complex"]
    #declare a list of probabilities corresponding to each superclass and pick one
    probabilities = [61/486, 287/486, 184/486]
    chosen_superclass = random.choices(superclasses, weights=probabilities, k=1)[0]
    if chosen_superclass == 'simple': #only (C)V or CV structures
        simple_onset = True 
    elif chosen_superclass == 'moderately_complex': #CVC, #CCV, #CCVC
        simple_onset = True 
        #roll with equal probability
        roll = random.randint(0, 2)
        if roll == 0:
            complex_onset = False
            simple_coda = True
        if roll == 1:
            complex_onset = True
            simple_coda = False
        else:
            complex_onset = False
            simple_coda = False
    else: #up to superhypercomplex, WIP for probabilities
        possible_outcomes = ['CCCV', 'CCCCV', 'CCVC', 'CCCVC', 'CCCCVC', 'CCVCC', 'CCCVCC', 'CCCCVCC', 'CVCCC', 'CCVCCC', 'CCCVCCC', 'CCCCVCCC', 'CVCCCC', 'CCVCCCC', 'CCCVCCCC', 'CCCCVCCCC']
        simple_onset = True
        selected_structure = random.choice(possible_outcomes)
        vowel_index = selected_structure.index('V')
        #assess onsets
        if vowel_index > 2 and selected_structure[vowel_index - 3] == 'C':
            supercomplex_onset = True
            if vowel_index > 3 and selected_structure[vowel_index - 4] == 'C':
                hypercomplex_onset = True
        else: complex_onset = False
        #assess codas
        if vowel_index < len(selected_structure) - 1 and selected_structure[vowel_index + 1] == 'C': 
            simple_coda = True
            if vowel_index < len(selected_structure) - 2 and selected_structure[vowel_index + 2] == 'C':
                complex_coda = True
                if vowel_index < len(selected_structure) - 3 and selected_structure[vowel_index + 3] == 'C':
                    supercomplex_coda = True
                    if vowel_index < len(selected_structure) - 4 and selected_structure[vowel_index + 4] == 'C':
                        hypercomplex_coda = True
        else: simple_coda = False
    #determine if onsets will be required or not as a global parameter
    mandatory_onset = bool()
    roll = random.randint(0, 1)
    if roll == 0:
        mandatory_onset = False
    else:
        mandatory_onset = True
    #store all the booleans in a .json
    syllable_parameters = {
        "simple_onset": simple_onset,
        "complex_onset": complex_onset,
        "supercomplex_onset": supercomplex_onset,
        "hypercomplex_onset": hypercomplex_onset,
        "simple_coda": simple_coda,
        "complex_coda": complex_coda,
        "supercomplex_coda": supercomplex_coda,
        "hypercomplex_coda": hypercomplex_coda,
        "mandatory_onset": mandatory_onset
    }
    #save the dictionary to a file
    with open('cache/syllable_parameters.json', 'w') as file:
        json.dump(syllable_parameters, file)

def encode_syllable_parameters():
    #read the syllable structure from a file as a list
    with open ('cache/syllable_structure.json') as s:
        syllable_structure = json.load(s)
    #open syllable parameters if they exist
    try:
        with open ('cache/syllable_parameters.json') as s:
            mandatory_onset = json.load(s)
    except FileNotFoundError:
        mandatory_onset = {}
    #index the syllable and declare all possible booleans
    vowel_index = syllable_structure.index('V') #find the index of the vowel in the syllable structure
    simple_onset = bool() #declare a boolean to store the simple onset
    complex_onset = bool() #declare a boolean to store the complex onset
    supercomplex_onset = bool() #declare a boolean to store the hypercomplex onset
    hypercomplex_onset = bool() #declare a boolean to store the superhypercomplex onset 
    simple_coda = bool() #declare a boolean to store the coda
    complex_coda = bool() #declare a boolean to store the complex coda
    supercomplex_coda = bool() #declare a boolean to store the hypercomplex coda
    hypercomplex_coda = bool() #declare a boolean to store the superhypercomplex coda
    mandatory_onset = bool() #declare a boolean to store the mandatory onset parameter
    #check for onsets
    if vowel_index > 0 and syllable_structure[vowel_index - 1] == 'C' or ')': 
        simple_onset = True
        if vowel_index > 1 and syllable_structure[vowel_index - 2] == 'C':
            complex_onset = True
            if vowel_index > 2 and syllable_structure[vowel_index - 3] == 'C':
                supercomplex_onset = True
                if vowel_index > 3 and syllable_structure[vowel_index - 4] == 'C':
                    hypercomplex_onset = True
    else:
        simple_onset = False
    #check for codas
    if vowel_index < len(syllable_structure) - 1 and syllable_structure[vowel_index + 1] == 'C': 
        simple_coda = True
        if vowel_index < len(syllable_structure) - 2 and syllable_structure[vowel_index + 2] == 'C':
            complex_coda = True
            if vowel_index < len(syllable_structure) - 3 and syllable_structure[vowel_index + 3] == 'C':
                supercomplex_coda = True
                if vowel_index < len(syllable_structure) - 4 and syllable_structure[vowel_index + 4] == 'C':
                    hypercomplex_coda = True
    else:
        simple_coda = False
    #print the results
    print ('Simple Onsets? ' + str(simple_onset))
    print ('Complex Onsets? ' + str(complex_onset))
    print ('Supercomplex Onsets? '+ str(supercomplex_onset))
    print ('Hypercomplex Onsets? '+ str(hypercomplex_onset))
    print ('Simple Codas? ' + str(simple_coda))
    print ('Complex Codas? '+ str(complex_coda))
    print ('Supercomplex Codas? '+ str(supercomplex_coda))
    print ('Hypercomplex Codas? '+ str(hypercomplex_coda))
    print ('Mandatory Onsets? '+ str(mandatory_onset))
    #declare the dictionary for saving
    onset_coda_dict = {
        "simple_onset": simple_onset,
        "complex_onset": complex_onset,
        "supercomplex_onset": supercomplex_onset,
        "hypercomplex_onset": hypercomplex_onset,
        "simple_coda": simple_coda,
        "complex_coda": complex_coda,
        "supercomplex_coda": supercomplex_coda,
        "hypercomplex_coda": hypercomplex_coda,
        "mandatory_onset": mandatory_onset
    }
    #save the dictionary to a file
    with open('cache/syllable_parameters.json', 'w') as file:
        json.dump(onset_coda_dict, file)

def decode_syllable_parameters ():
    #open and read syllable_structure.json
    with open ('cache/syllable_parameters.json') as s:
        syllable_structure = json.load(s)
    #define the structure
    CV_structure = []
    complete = False
    #append data from syllabe_structure.json to CV_structure
    while complete == False:
        if syllable_structure['hypercomplex_onset'] == True: 
            CV_structure.append('CCCC')
        elif syllable_structure['supercomplex_onset'] == True:
            CV_structure.append('CCC')
        elif syllable_structure['complex_onset'] == True:
            CV_structure.append('CC')
        elif syllable_structure['simple_onset'] == True:
            CV_structure.append('C')
        else:
            pass
        CV_structure.append('V')
        if syllable_structure['hypercomplex_coda'] == True:
            CV_structure.append('CCCC')
        elif syllable_structure['supercomplex_coda'] == True:
            CV_structure.append('CCC')
        elif syllable_structure['complex_coda'] == True:
            CV_structure.append('CC')
        elif syllable_structure['simple_coda'] == True:
            CV_structure.append('C')
        else:
            pass
        complete = True
    syllable_structure = ''.join(CV_structure)
    print ('\nGenerated structure: ' + syllable_structure)

def main ():
    print ('\nSYLLABLE STRUCTURE\n')
    #ask the user if they would like to modify syllable structure themselves, or have one generated
    task = input('Would you like to: a) generate a syllable structure, or b) input your own? \n')
    while True:
        if task == 'a':
            generate_syllable_structure()
            decode_syllable_parameters()
            break
        elif task == 'b':
            request_syllable()
            encode_syllable_parameters()
            break
        else:
            print('Invalid input. Please try again.')
