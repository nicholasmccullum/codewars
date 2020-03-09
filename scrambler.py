cramble(s1, s2):
    for letter in list(s2):
        doesLetterMatch = False
        
        i= 0
        while i < len(list(s1)):
            if(list(s1)[i] == letter):
                doesLetterMatch = True
                break
            i += 1
        if(doesLetterMatch == False):
            return doesLetterMatch
    return doesLetterMatch
