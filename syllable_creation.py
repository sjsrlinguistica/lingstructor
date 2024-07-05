import random
import json
import utilities

#paths to the json files
phonemes_path = utilities.get_phonemes_path()
syllable_parameters_path = utilities.get_syllable_parameters_path()
syllable_structure_path = utilities.get_syllable_structure_path()


with open(phonemes_path) as p:
    phonemes = json.load(p)
with open (syllable_parameters_path) as s:
    syllable_parameters = json.load(s)
with open (syllable_structure_path) as p:
    syllable_structure = json.load(p)

vowels = phonemes['vowels']
consonants = phonemes['consonants']

def gen_vowel(): #WIP
    vowel = random.choice(vowels)
    return vowel

def gen_onset():
    unjoined_onset = []
    if syllable_parameters['mandatory_onset']:
        unjoined_onset.append(random.choice(consonants))
        if syllable_parameters['complex_onset'] and random.choice([True, False]):
            unjoined_onset.append(random.choice(consonants))
            if syllable_parameters['supercomplex_onset'] and random.choice([True, False]):
                unjoined_onset.append(random.choice(consonants))
                if syllable_parameters['ultracomplex_onset'] and random.choice([True, False]):
                    unjoined_onset.append(random.choice(consonants))
    else:
        roll = random.choice([True, False])
        if roll is True:
            unjoined_onset.append(random.choice(consonants))
            if syllable_parameters['complex_onset'] and random.choice([True, False]):
                unjoined_onset.append(random.choice(consonants))
                if syllable_parameters['supercomplex_onset'] and random.choice([True, False]):
                    unjoined_onset.append(random.choice(consonants))
                    if syllable_parameters['ultracomplex_onset'] and random.choice([True, False]):
                        unjoined_onset.append(random.choice(consonants))
    onset = ''.join(unjoined_onset)
    return onset

def gen_coda():
    unjoined_coda = []
    if syllable_parameters['simple_coda'] and random.choice([True, False]):
        unjoined_coda.append(random.choice(consonants))
        if syllable_parameters['complex_coda'] and random.choice([True, False]):
            unjoined_coda.append(random.choice(consonants))
            if syllable_parameters['supercomplex_coda'] and random.choice([True, False]):
                unjoined_coda.append(random.choice(consonants))
                if syllable_parameters['ultracomplex_coda'] and random.choice([True, False]):
                    unjoined_coda.append(random.choice(consonants))
    coda = ''.join(unjoined_coda)
    return coda

def create_syllable():
    syllable = []
    #check for mandatory onset
    onset = gen_onset()
    syllable.append(onset)
    vowel = random.choice(vowels)
    syllable.append(vowel)
    coda = gen_coda()
    syllable.append(coda)
    syllable = ''.join(syllable)
    return syllable