comprised nded_form(num):
    digitCount = len(str(num));
    finalNum = "";
    i = 0;
    while i < digitCount:
        expandedDigit = str(num)[i];
        print(expandedDigit);
        if(expandedDigit != "0"):
            zerosRequired = digitCount - i - 1;
            x = 0;
            while x < zerosRequired:
                expandedDigit = expandedDigit + "0"
                x += 1;
            finalNum = finalNum + ' + ' + expandedDigit;
        i += 1;    
    return finalNum[3:];
