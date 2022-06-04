def filter_long_words(sentence, n):
    c = []
    for b in sentence.split():
        if len(b) > int(n):
            c.append(b)
    #return c
    print(c)
            


filter_long_words("The quick brown fox jumps over the lazy dog", 4)
#c = "The quick brown fox jumps over the lazy dog"
#d = c.split()
#print(c)

#def filter_long_words(sentence, n):
#    return [word for word in sentence.split() if len(word) > n]