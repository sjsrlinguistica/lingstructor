#imports
import json
import wordfreq
from nltk import pos_tag
import nltk
import random
import numpy as np
import scipy.stats as stats
import syllable_creation
import csv

#nltk.download('averaged_perceptron_tagger') # MOVE THIS TO BEING A DEPENDENCY!!!!

def generate_origin_lexemes():
    #ask the uset to input their chosen language (FUTURE FEATURE)
    #ask the user how many words they would like
    while True:
        try:
            requested_num = int(input('How many words would you like to generate? ')) #ADD A DISCLAIMER THAT THIS TARGET MAY NOT BE MET AS THE FIRST 300-400 WORDS CONTAIN MANY GRAMMATICAL ITEMS
            break
        except ValueError:
            print ('Please enter a valid number.')
    #generate a list of the 100 most common words in the English language
    common_words = wordfreq.top_n_list('en', requested_num*1.5)
    #identify the part of speech of each item in common_words
    pos_tags = pos_tag(common_words)
    tag_dict = dict(zip(common_words, pos_tags))
    #identify which POS tags to include in the list of lexemes
    included_POS = ['CD', 'JJ', 'LS', 'MD', 'NN', 'RB', 'UH', 'VB']
    cleaned_lexemes = [] #declare a list to store the cleaned lexemes
    nltk_abnormalities = ['i', "i'm"] #get rid of weird artifacts from the nltk tagger
    for word, tag in tag_dict.items():
        if tag[1] in included_POS:
            if tag[0] in nltk_abnormalities:
                pass
            elif "'" in tag[0]: #remove english contractions as artifacts
                pass
            else:
                cleaned_lexemes.append(word)
        else:
            pass
    #find frequency of each word in the list
    lexeme_frequency_dict = {}
    for word in cleaned_lexemes:
        frequency = wordfreq.word_frequency(word, 'en')
        lexeme_frequency_dict[word] = float(frequency)
    # Normalize frequencies to a normal distribution.
    linear_probabilities = lexeme_frequency_dict.values()
    # Ask user to detemine mean word length for the language and use the frequencies to apply a noromal distrbution.
    mean_syllables = float(input("Enter the mean number of syllables per word you would like: "))
    std_dev = 1 
    num_samples = len(linear_probabilities)
    norm_samples = np.random.normal(mean_syllables, std_dev, num_samples)
    # Sort linear probabilities
    sorted_linear_probs = sorted(linear_probabilities)
    # Compute cumulative probabilities
    cumulative_probs = np.linspace(0, 1, num_samples)
    # Use normal distribution PPF (Percent Point Function, inverse CDF) to transform linear probs
    transformed_values = stats.norm.ppf(cumulative_probs, loc=mean_syllables, scale=std_dev)
    list_transformed_values = transformed_values.tolist()

    #replace the frequencies in lexeme_frequency_dict with the transformed values
    for word, freq in lexeme_frequency_dict.items():
        lexeme_frequency_dict[word] = list_transformed_values.pop(0)
    #return the normalized lexemes
    return lexeme_frequency_dict

def create_syllable_targets(lexeme_frequency_dict):
    syllable_targets = []
    for lexeme, frequency in lexeme_frequency_dict.items():
        if frequency < 0.5:
            syllable_target = 1
            syllable_targets.append(syllable_target)
        elif frequency < 1:
            #generate a random number between 1 and 2
            syllable_target = random.randint(1, 2)
            syllable_targets.append(syllable_target)
        else: 
            roun_coin = random.randint(0, 1)
            if roun_coin == 0:
                syllable_target = np.floor(frequency) if np.isfinite(frequency) else max(syllable_targets)  # Default to max if not finite
                syllable_targets.append(syllable_target)
            else:
                syllable_target = np.ceil(frequency) if np.isfinite(frequency) else max(syllable_targets)  # Default to max if not finite
                syllable_targets.append(syllable_target)
            
    #eliminate all decimals
    syllable_targets = [int(i) for i in syllable_targets]
    #create a dictionary of lexemes and their syllable targets
    lexeme_syllable_dict = dict(zip(lexeme_frequency_dict.keys(), syllable_targets))
    #print the dictionary
    return lexeme_syllable_dict
    
def create_words(lexeme_syllable_dict):
    words = []
    for lexeme, syllable_target in lexeme_syllable_dict.items():
        word = []
        for i in range(syllable_target):
            syllable = syllable_creation.create_syllable()
            word.append(syllable)
        joined_word = ''.join(word)
        words.append(joined_word)
        print (joined_word)
    #match words to lexemes in a dictionary
    lexicon = dict(zip(words, lexeme_syllable_dict.keys()))
    print (lexicon)
    return lexicon

def assign_lexemes(normalized_lexemes): #if the user wants to assign lexemes to blank words, currently unused
    with open('cache/generated_words.json') as file:
       blank_words = json.load(file)
    selected_lexemes = []
    for word in blank_words:
        #select a random word from normalized_lexemes
        selected_lexeme = random.choice(list(normalized_lexemes.keys()))
        #assign the selected word to the blank word
        selected_lexemes.append(selected_lexeme)
        #remove the selected word from normalized_lexemes
        del normalized_lexemes[selected_lexeme]
    #pair the selected word with the blank word in a dictionary
    lexicon = dict(zip(blank_words, selected_lexemes))
    return lexicon

def clean_tags(tag):
    tag = str(tag)
    if tag == 'CD':
        cleaned_tag = ('N')
    elif tag == 'JJ':
        cleaned_tag = ('Adj')
    elif tag == 'LS':
        cleaned_tag = ('N')
    elif tag == 'MD':
        cleaned_tag = ('V')
    elif tag == 'NN':
        cleaned_tag = ('N')
    elif tag == 'RB':
        cleaned_tag = ('Adv')
    elif tag == 'UH':
       cleaned_tag = ('Intj')
    elif tag == 'VB':
        cleaned_tag = ('V')
    else:  
        cleaned_tag = ('Unknown') #issue to fix later; NTLK identifies another POS initially
    return cleaned_tag

def create_lexicon_csv (lexicon):
    # Initialize a list to hold word, lexeme, and pos
    lexicon_with_pos = []
    # create  list of pos tags from the lexicon lexemes
    lexemes = lexicon.values()
    pos_tags = pos_tag(lexemes)
    cleaned_tags = []
    for i in pos_tags:
        cleaned_tag = clean_tags(i[1])
        cleaned_tags.append(cleaned_tag)
    lexicon_with_pos = list(zip(lexicon.keys(), lexicon.values(), cleaned_tags))
    # Save lexicon with pos to a csv file
    with open('output/lexicon.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Word', 'meaning', 'Part of Speech']) # Write the header
        for word, lexeme, pos in lexicon_with_pos: # Write the lexicon data
            writer.writerow([word, lexeme, pos])

def generate_lexicon():
    lexeme_frequency_dict = generate_origin_lexemes()
    lexeme_syllable_dict=create_syllable_targets(lexeme_frequency_dict)
    lexicon = create_words(lexeme_syllable_dict)
    create_lexicon_csv(lexicon)
    return lexicon


