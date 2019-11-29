# to begin we start with a list of words in a file called spell.words
# we read the file and strip out the file endings
words = open('spell.words').readlines()
words = map(lambda x: x.strip(), words)
# now check if the word zygotic is a word
#print('zygotic' in words)


# Check a Word
def load_words(file_name):
    words = open(file_name).readlines()
    return list (map(lambda x: x.strip(), words))

def check_word(words, word):
    return word in words

###### words = load_words('spell.words')
# now check if the word zygotic is a word
###### print(check_word(words, 'zygotic'))

# Check a sentence
def check_words(words, sentence):
    words_to_check = sentence.split(' ')
    for word in words_to_check:
        if not check_word(words, word):
            print('Word is misspelt : ' + word)
            return False
    return True

#words = load_words('spell.words')
#print(check_word(words, 'zygotic'))
print(check_words(words, 'zygotic mistasdas elementary'))



