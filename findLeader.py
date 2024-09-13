def findLeader_array(arr):
    n = len(arr)
    
    if n== 0:
        return []
    leaders = []
    maxRight = arr[-1]
    leaders.append(maxRight)
    
    for i in range(n-2,-1,-1):
        if arr[i] > maxRight  :
            leaders.append(arr[i])
            maxRight = arr[i]
            
    leaders.reverse()
    return leaders





# give input in the format [1, 2, 4, 5, 4]
print("enter your array")
arr = input().strip("[]")
array = list(map(int,arr.split(',')))
result = findLeader_array(array)
print(result)
