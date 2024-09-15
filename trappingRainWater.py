def trap(height):
    if not height or len(height)<3:
        return 0
    
    left, right = 0, len(height)-1
    left_max, right_max = height[left], height[right]
    total_water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                total_water +=left_max-height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                total_water +=right_max-height[right]
            right -= 1
    
    return total_water





# give input in the format [1, 2, 4, 5, 4]
print("enter your histogram array of heights")
arr = input().strip("[]")
array = list(map(int,arr.split(',')))
result = trap(array)
print(result)
