bonacci(signature, n):
    if(n==0):
        return []
    if(n==1):
        return signature[:1]
    if(n==2):
        return signature[:2]
    if(n==3):
        return signature[:3]
    
    tribonacciSequence = signature.copy()
    while len(tribonacciSequence) < n:
        tribonacciSequence.append(tribonacciSequence[-1] + tribonacciSequence[-2] + tribonacciSequence[-3])
    return tribonacciSequence
