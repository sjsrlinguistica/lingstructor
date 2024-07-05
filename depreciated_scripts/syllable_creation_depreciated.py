import random
import json

with open('cache/phonemes.json') as p:
    phonemes = json.load(p)
with open ('cache/syllable_structure.json') as s:
    syllable_structure = json.load(s)

counter = 0 
requested_num = 50 #move to user input
syllables = []
vowels = phonemes['vowels']
consonants = phonemes['consonants']

#import probabilities
prob_simple_onset = 0.5

def create_syllable():
    global counter #declare the countr within the function
    syllable = [] #declare a syllable object
    syllable_types = ["V", "CV", "CCV", "CCCV", "VC", "CVC", "CCVC", "CCCVC", "VCC", "CVCC", "CCVCC", "CCCVCC", "VCCC", "CVCCC", "CCVCCC", "CCCVCCC"]
    # List of probabilities corresponding to each syllable
    probabilities = [0.3, 0.5, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Randomly choose one event based on the specified probabilities
    chosen_event = random.choices(syllable_types, weights=probabilities, k=1)[0]
    if chosen_event == 'V':
        syllable.append(random.choice(vowels))
        joined_syllable = ''.join(syllable)
        syllables.append(joined_syllable)
        counter += 1
    elif chosen_event == 'CV':
        syllable.append(random.choice(consonants))
        syllable.append(random.choice(vowels))
        joined_syllable = ''.join(syllable)
        syllables.append(joined_syllable)
        counter += 1
    elif chosen_event == 'CCV':
        syllable.append(random.choice(consonants))
        syllable.append(random.choice(consonants))
        syllable.append(random.choice(vowels))
        joined_syllable = ''.join(syllable)
        syllables.append(joined_syllable)
        counter += 1
    elif chosen_event == 'CCCV':
        syllable.append(random.choice(consonants))
        syllable.append(random.choice(consonants))
        syllable.append(random.choice(consonants))
        syllable.append(random.choice(vowels))
        joined_syllable = ''.join(syllable)
        syllables.append(joined_syllable)
        counter += 1
    elif chosen_event == 'VC':
        syllable.append(random.choice(vowels))
        syllable.append(random.choice(consonants))
        joined_syllable = ''.join(syllable)
        syllables.append(joined_syllable)
        counter += 1
    elif chosen_event == 'CVC':
        syllable.append(random.choice(consonants))
        syllable.append(random.choice(vowels))
        syllable.append(random.choice(consonants))
        joined_syllable = ''.join(syllable)
        syllables.append(joined_syllable)
        counter += 1
    else: 
        pass

while counter < requested_num:
    create_syllable()
else:
    pass
    print(syllables)

#append the syllables to generated_syllables.json file
with open('cache/generated_syllables.json', 'w') as file:
    json.dump(syllables, file)

