
g_it(text):
    pigLatinString = ''
    for word in text.split(" "):
        word = word + word[:1]
        word = word[1:]
        if (word != "." and word != "?" and word != "!"):
            word = word + 'ay'
        pigLatinString = pigLatinString + word + ' '
    return pigLatinString[:(len(pigLatinString)-1)]
