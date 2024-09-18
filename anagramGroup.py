def anagramGroup(strs):
    anagrams = {}  
    
    for s in strs:
        key = ''.join(sorted(s))
        if key not in anagrams:
            anagrams[key] = []
            
        anagrams[key].append(s)
  
    return list(anagrams.values())

print("enter your strings with a space in between")
array = list(map(str,input().split()))
result = anagramGroup(array)
print(result)

