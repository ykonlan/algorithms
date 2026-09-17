class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(6)

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

def post_order_traversal(node:TreeNode):
    current = node
    stack = []
    seen = set()
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        peeked = stack[-1]
        if peeked.right and peeked.right not in seen:
            current = peeked.right
            seen.add(peeked.right)
        else:
            popped = stack.pop()
            print(popped)
    return

def pre_order_traversal(node:TreeNode):
    stack = [node]
    while stack:
        current = stack.pop()
        print(current)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return
    


    
print(pre_order_traversal(A))