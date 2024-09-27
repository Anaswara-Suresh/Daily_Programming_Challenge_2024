def evaluate_postfix(tokens):
    stack=[]
    
    for token in tokens:
        if token in '+-*/^':  
            b = stack.pop()
            a = stack.pop()
            
            
            if token == '+':
                stack.append(a+b)
            elif token == '-':
                stack.append(a-b)
            elif token == '*':
                stack.append(a*b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Division by zero is undefined.")
                stack.append(int(a/b))
            elif token == '^':  
                stack.append(a**b)
        else:
            stack.append(int(token))

    return stack[0]



print("Input the postfix expression (space-separated):")
N = input().split()
result = evaluate_postfix(N)
print(f"Result: {result}")
