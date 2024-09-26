
def count_divisors(N):
    divisors_count=0
    
   
    for i in range(1, int(pow(N,0.5))+1):
        if N % i == 0:
            divisors_count += 1
            if i != N//i:
                divisors_count += 1
    
    return divisors_count

print("Input the Number:")
N = int(input())

result = count_divisors(N)
print("No of factors of the given number:", result)
