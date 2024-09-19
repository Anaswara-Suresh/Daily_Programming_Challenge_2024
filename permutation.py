def swapChars(s, i, j):
    s_list = list(s)
    s_list[i], s_list[j] = s_list[j], s_list[i]
    return ''.join(s_list)

def generatePermutationsRec(string, startIdx, result):
    if startIdx == len(string) - 1:
        result.append(string)
        return
    
    for currentIdx in range(startIdx, len(string)):
        string = swapChars(string, startIdx, currentIdx)
        generatePermutationsRec(string, startIdx + 1, result)
        string = swapChars(string, startIdx, currentIdx)

def generatePermutations(string):
    result = []
    generatePermutationsRec(string, 0, result)
    return result

print("Enter your string:")
input_string = input().strip()
result = generatePermutations(input_string)
print(result)
