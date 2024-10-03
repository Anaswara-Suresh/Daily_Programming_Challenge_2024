class Node:
    def __init__(self,v=0,l=None,r=None):
        self.v=v
        self.l=l
        self.r=r

def isBST(root: Node) -> bool:
    def chk(n, lo=float('-inf'), hi=float('inf')):
        if not n:
            return True
        if not (lo < n.v < hi):
            return False
        return chk(n.l,lo,n.v) and chk(n.r,n.v,hi)
    return chk(root)


def build_tree(level_order):
    if not level_order or level_order[0] is None:
        return None

    root = Node(level_order[0])
    queue = [root]
    i = 1

    while i <len(level_order):
        current= queue.pop(0)

     
        if i <len(level_order) and level_order[i] is not None:
            current.l = Node(level_order[i])
            queue.append(current.l)
        i += 1

        if i <len(level_order) and level_order[i] is not None:
            current.r = Node(level_order[i])
            queue.append(current.r)
        i += 1

    return root


level_order_input =input("Enter the level-order representation of the tree (comma separated, use 'None' for null nodes): ")
level_order_list =[int(x) if x != 'None' else None for x in level_order_input.split(',')]


root = build_tree(level_order_list)


print(isBST(root))
