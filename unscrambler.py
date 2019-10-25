def convert_to_list():
    file = 'scrambled_words.txt'
    scrambled_words_list = []
    with open(file, 'r') as f:
        for word in f:
            word = word[:-1].lower()
            scrambled_words_list.append(word)
    return scrambled_words_list

def dictionary():
    word_list = []
    file = 'sowpods.txt'
    with open(file, 'r') as f:
        for word in f:
            word = word[:-1].lower()
            word_list.append(word)
    return word_list


def unscramble():
    for scrambled_word in convert_to_list():
        sowpods = dictionary()
        for word in convert_to_list():
            for i in sowpods:
                if sorted(word) == sorted(i):
                    print(i, end=', ')
                    break
        break


unscramble()







