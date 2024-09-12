def merge_array(arr1,arr2):
    m,n = len(arr1), len(arr2)
    for i in range(m):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
            first = arr2[0]
            k=1
            while k<n and arr2[k]<first:
                arr2[k-1] = arr2[k]
                k +=  1
            arr2[k-1] = first
            
    return arr1,arr2





# give input in the format [1, 2, 4, 5, 4]
print("enter your first array")
arr = input().strip("[]")
array1 = list(map(int,arr.split(',')))
print("enter your second array")
arr = input().strip("[]")
array2 = list(map(int,arr.split(',')))
arr1_sorted, arr2_sorted = merge_array(array1, array2)
print("Merged arr1:", arr1_sorted)
print("Merged arr2:", arr2_sorted)
