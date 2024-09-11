def duplicate_no(arr):
    
    fast = arr[0]
    slow = arr[0]
    
    
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    
    
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    
    return slow


# give input in the format [1, 2, 4, 5, 4]
arr = input().strip("[]")
array = list(map(int,arr.split(',')))
print(duplicate_no(array))