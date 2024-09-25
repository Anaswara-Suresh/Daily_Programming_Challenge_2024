def primeFactors(N):
    factors = []
    
    
    while N % 2 == 0:
        factors.append(2)
        N //= 2  

    for i in range(3, int(N**0.5) + 1, 2):
        while N % i == 0:
            factors.append(i)
            N //= i  
    
    if N > 2:
        factors.append(N)
    
    return factors


print("Input the Number:")
N = int(input())

result = primeFactors(N)
print("Prime factors of the given number:", result)
