comprised rentheses(string):
    #parenthesesCounter should be 0 at the end of the function to return True
    #In addition, parenthesesCounter can never be negative, or the function will 
    #break and return false
    parenthesesCounter = 0
    for x in list(string):
        if x == '(':
            parenthesesCounter += 1
        if x == ')':
            parenthesesCounter -= 1
        if (parenthesesCounter < 0):
            return False
    return parenthesesCounter == 0
