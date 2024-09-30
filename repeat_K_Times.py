def repeat_K_Times(arr, k):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

 
    for num in arr:
        if frequency[num] == k:
            return num

   
    return -1


print("Enter the numbers in array with space in between.")
N=input().split()
arr=[int(x) for x in N]
print("Enter the threshhold ")
k = int(input())
result = repeat_K_Times(arr,k)
if result == -1:
    print("No such number present in array that repeats K times.")
else:
    print(result)