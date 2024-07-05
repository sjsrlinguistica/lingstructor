#import data from generated_syllables.json
import json, random
with open('cache/generated_syllables.json') as file:
     syllables = json.load(file)

#declare a list of words
words = []

#request user input for the number of words to generate
requested_num = int(input('How many words would you like to generate? '))

# Create a word by combining random syllables
def create_word():
    word = []
    word_length = random.randint(1, 5)
    for i in range(word_length):
        word.append(random.choice(syllables))
        joined_word = ''.join(word)
    words.append(joined_word) #append the word to the list
    return words

#keep count of words
while len(words) < requested_num:
    create_word()
else:
    pass

#append the syllables to generated_words.json file
with open('cache/generated_words.json', 'w') as file:
    json.dump(words, file)

