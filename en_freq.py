import wordfreq

# Generate and retrieve the English frequency dictionary
words = wordfreq.top_n_list('en', 1000, wordlist='best')

#calculate frequencies
freqs = []
for word in words:
    freq=wordfreq.word_frequency(word, "en")
    freqs.append(freq)

#create a dictionary of output and freqs
output = dict(zip(words, freqs))
print(output)