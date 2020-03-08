nagrams(wordToAnagram, words):
    anagramArray = []
    for word in words:
        if(sorted(wordToAnagram)  == sorted(word)):
            anagramArray.append(word)
    return anagramArray
