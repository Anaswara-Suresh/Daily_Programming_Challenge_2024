def revString(array):
    n = len(array)-1
    for i in range(n,-1,-1):
            print(array[i],"",end='')
    return 0


print("enter your string")
array = list(map(str,input().split()))
result = revString(array)

