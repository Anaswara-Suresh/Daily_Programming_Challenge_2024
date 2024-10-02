class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        
        left=self.lowestCommonAncestor(root.left, p, q)
        right=self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left if left else right

def insert_level_order(arr, root, i, n):
    if i<n:
        temp=TreeNode(arr[i]) if arr[i] is not None else None
        root=temp

        if root is not None:
            root.left=insert_level_order(arr, root.left, 2 * i + 1, n)
            root.right=insert_level_order(arr, root.right, 2 * i + 2, n)

    return root

def find_node(root, val):
    if root is None:
        return None
    if root.val==val:
        return root
    left=find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)


arr=list(map(int, input("Enter the elements of the tree (use -1 for None nodes): ").split()))
p_val=int(input("Enter the value of node p: "))
q_val=int(input("Enter the value of node q: "))


arr = [None if x == -1 else x for x in arr]

root = insert_level_order(arr, None, 0, len(arr))


p = find_node(root,p_val)
q = find_node(root,q_val)


solution = Solution()
lca = solution.lowestCommonAncestor(root, p, q)

if lca:
    print(f"The Lowest Common Ancestor of {p_val} and {q_val} is: {lca.val}")
else:
    print("Lowest Common Ancestor not found.")
