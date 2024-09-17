def commonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
   
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix


print("enter your strings with a space in between")
array = list(map(str,input().split()))
result = commonPrefix(array)
print(result)

