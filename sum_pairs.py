def sum_pairs(ints, s):
    i = 0
    while i < len(ints)-1:
        if(ints[i]+ints[i+1] == s):
            return [ints[i], ints[i+1]]
        i += 1
