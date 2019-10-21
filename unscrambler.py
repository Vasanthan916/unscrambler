

def dictionary():

    word_list = []
    file = 'sowpods.txt'
    with open(file, 'r') as f:
        for word in f:
            word = word[:-1].lower()
            word_list.append(word)
    return word_list



def unscramble(scrambled_list):

    for scrambled_word in scrambled_list:
        sowpods = dictionary()
        for word in scrambled_list:
            for i in sowpods:
                if sorted(word) == sorted(i):
                    print(i)
                    break
        break
unscramble(['dnashciw'])







