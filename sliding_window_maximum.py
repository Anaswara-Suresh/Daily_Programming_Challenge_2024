def sliding_window_maximum(arr, k):
    n = len(arr)
    if n == 0:
        return []
    dq = []  
    result = []
    
    for i in range(n):
        
        if dq and dq[0] < i - k + 1:
            dq.pop(0)
        
        
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
       
        dq.append(i)
        
       
        if i >= k - 1:
            result.append(arr[dq[0]])  
    
    return result


print("Enter the numbers in array with space in between.")
N=input().split()
arr=[int(x) for x in N]
print("Enter the window size(k) ")
k = int(input())
result = sliding_window_maximum(arr,k)
print(result)