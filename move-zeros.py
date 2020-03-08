(array):
    zeroCounter = 0
    modifiedArray = []
    for x in array:
        if(x == 0):
            zeroCounter += 1
            pass
        else:
            modifiedArray.append(x)
    print(zeroCounter)
    i = 0
    if(zeroCounter != 0):
        while i < zeroCounter:
            modifiedArray.append(0)
            i+=1
    return modifiedArray
