def find_zero_sum(arr):
    prefix_map = {}
    result = []

    prefix_sum = 0
    prefix_map[0]=[-1]
    for i in range(len(arr)):
        prefix_sum += arr[i]
        

        if prefix_sum in prefix_map:
            for start_index in prefix_map[prefix_sum]:
                result.append((start_index+1, i))
        
   
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = []
        prefix_map[prefix_sum].append(i)
    
    return result




# give input in the format [1, 2, 4, 5, 4]
print("enter your array")
arr = input().strip("[]")
array = list(map(int,arr.split(',')))
result = find_zero_sum(array)
print(result)
