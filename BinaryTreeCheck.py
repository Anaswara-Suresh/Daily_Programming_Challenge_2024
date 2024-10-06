class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    if not root:
        return True
    

    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))
    
    return is_mirror(root.left, root.right)

root1 = TreeNode(1)
root1.left = TreeNode(2, TreeNode(3), TreeNode(4))
root1.right = TreeNode(2, TreeNode(4), TreeNode(3))

root2 = TreeNode(1)
root2.left = TreeNode(2, None, TreeNode(3))
root2.right = TreeNode(2, None, TreeNode(3))

root3 = TreeNode(1)

root4 = None

root5 = TreeNode(1)
root5.left = TreeNode(2, TreeNode(3))
root5.right = TreeNode(2, None, TreeNode(3))

print(is_symmetric(root1))  
print(is_symmetric(root2))  
print(is_symmetric(root3))  
print(is_symmetric(root4))  
print(is_symmetric(root5))  
