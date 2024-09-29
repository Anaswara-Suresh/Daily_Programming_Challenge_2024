def reverseStack(stack):
    if not stack:
        return
    top = stack.pop()
    reverseStack(stack)
    insertAtBottom(stack, top)


def insertAtBottom(stack, element):
    if not stack:
        stack.append(element)
        return
    top = stack.pop()
    insertAtBottom(stack, element)
    stack.append(top)


N=input().split()
stack=[int(x) for x in N]
reverseStack(stack)
print(stack)
