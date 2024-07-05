import random
import json

#import phonemes and syllable structure from phonemes.txt and syllable_structure.txt
with open('phonemes.json', 'r') as file:
#import the phoneme lists
    phonemes = json.load(file)
    vowels = phonemes['vowels']
    consonants = phonemes['consonants']

with open('syllable_structure.json', 'r') as file:
    #import the syllable structure
    syllable_structure = json.load(file)
    simple_onset = syllable_structure['simple_onset']
    simple_coda = syllable_structure['simple_coda']
    complex_onset = syllable_structure['complex_onset']
    complex_coda = syllable_structure['complex_coda']

#determining probabilities
print ('The program will generate random probabilities for syllable frequncies based on the syllable structure and real-world tendencies. \n You the user will be prompted to edit these if you choose.')

#V syllable probabilities
if simple_onset == False and simple_coda == False: #only v structures
    prob_v = 1
elif (simple_onset and not simple_coda) or (simple_coda and not simple_onset): #if there is only simple syllable (only onsets or only codas)
    prob_v = random.triangular(0.55, 0.5, 0.40) #triangular random number
    prob_cv = 1 - prob_v
    prob_vc = prob_cv
elif (simple_onset and simple_coda) and (not complex_onset) and (not complex_coda):#simple onsets and simple codas
    prob_v = random.triangular(0.15, 0.35, 0.25)
    probvar = random.triangular(1, 2, 1.5)
    prob_cv = ((1-prob_v) * (1/probvar))
    prob_vc = (1-prob_v-prob_cv)
    prob_dict = {
    "V": prob_v,
    "CV": prob_cv,
    "VC": prob_vc
    }
    with open("syllable_structure.txt", "r+") as file:
        lines = file.readlines()
        lines = lines[:9] + ["\n"] * (9 - len(lines))  # Add empty lines until line 9
        for key, value in prob_dict.items():
            lines.append(f"{key}: {value}\n")  # Append probabilities
        file.seek(0)
        file.writelines(lines)
        file.close()
        print(lines)
    for key, value in prob_dict.items(): #print output
        print("Probability of " + key + ":", round(value, 20))
elif simple_onset and (complex_onset or simple_coda): #if there are moderately complex syllables (complex onsets, onsets and codas)
    prob_v = random.triangular(0.15, 0.35, 0.25)
    prob_cv = random.triangular(0.15, 0.35, 0.25)
    prob_vc = prob_cv/random.triangular(1.5, 2.5, 2)
    probvar = (1-prob_v-prob_cv-prob_vc)
    prob_cvc = probvar * 0.4
    prob_ccv = probvar * 0.4
    prob_ccvc = probvar * 0.2
    #print probabilities
    print("Probability of V:", round(prob_v, 2))
    print("Probability of CV:", round(prob_cv, 2))
    print("Probability of VC:", round(prob_vc, 2))
    print("Probability of CVC:", round(prob_cvc, 2))
    print("Probability of CCV:", round(prob_ccv, 2))
    print("Probability of CCVC:", round(prob_ccvc, 2))
    #print the sum of the probabilities of this elif section
    prob = prob_v + prob_cv + prob_vc + prob_cvc + prob_ccv + prob_ccvc
    print (prob)
else: #presumes very complex syllables
    print ('Syllables this long are not yet supported!') #if there are any very complex syllables (multiple codas, triple onsets)