def bal(s):
    stk = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in pairs:
            top = stk.pop() if stk else '#'
            if pairs[ch] != top:
                return False
        else:
            stk.append(ch)
    return not stk
tests = ["()", "([)]", "[{()}]", ""]
for i, t in enumerate(tests):
    print(f"Test Case {i + 1}: Input: {t}")
    print("Output:", "true" if bal(t) else "false")
    print()

print("Enter your string:")
input_string = input().strip()
result = bal(input_string)
print(result)
