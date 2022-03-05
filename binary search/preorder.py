# Binary search pre order trvaversal works like -> Root - Left - Right

class Tree:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)




tree = Tree(1)
tree.left = Tree(2)
tree.right = Tree(3)
tree.left.left = Tree(4)
tree.left.right = Tree(5)
preorder(tree)






