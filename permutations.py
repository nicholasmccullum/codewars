#This is the correct answer to the Shopify technical interview quesiton.

def permutations(s):
    if s[0] == "?":
        res = permutations(s[1:])
        return ["0" + x for x in res] + ["1" + x for x in res]
    else: 
        return [s[0] + x for x in permutations(s[1:])]
    
print(permutations("?0?"))
