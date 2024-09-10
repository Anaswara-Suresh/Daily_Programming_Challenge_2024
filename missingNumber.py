def missing_no(arr):
    n = len(arr) +1
    sumArray = sum(arr)
    actualSum =  (n*(n+1))//2
    missingNumber = actualSum-sumArray
    print("Missing Number: ",missingNumber)        
    return 0


# give input in the format [1, 2, 4, 5]
arr = input().strip("[]")
array = list(map(int,arr.split(',')))
missing_no(array)