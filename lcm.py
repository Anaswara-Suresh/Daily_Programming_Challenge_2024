def gcd(N,M):
   
    while M != 0:
        N, M = M, N % M
    return N

def lcm(N,M):
 
    return (N*M)//gcd(N,M)

print("Input first Number:")
N = int(input())
print("Input second Number:")
M = int(input())

result = lcm(N,M)
print("LCM of given numbers:", result)
