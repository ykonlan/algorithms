class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

A = TreeNode(1)
B = TreeNode(4)
C = TreeNode(5)
D = TreeNode(6)
E = TreeNode(7)
F = TreeNode(8)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F


def in_order_traversal(node:TreeNode):
    stack = []
    current = node
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        the_node = stack.pop()
        current = the_node.right
        print(the_node)
    return
    
print(in_order_traversal(A))