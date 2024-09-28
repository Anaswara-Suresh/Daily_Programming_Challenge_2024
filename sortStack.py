def insert_in_sorted_order(stack, element):
    if len(stack)==0 or stack[-1]<=element:
        stack.append(element)
        return
    top_element=stack.pop()
    insert_in_sorted_order(stack, element)
    stack.append(top_element)

def sort_stack(stack):
    if len(stack)==0:
        return
    top_element=stack.pop()
    sort_stack(stack)
    insert_in_sorted_order(stack,top_element)

N=input().split()
stack=[int(x) for x in N]
sort_stack(stack)
print(stack)
