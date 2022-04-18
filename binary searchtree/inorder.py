class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def buildTree(self,data):
        if data == self.data:
            return
        
        # add node in left
        if data < self.data:
            if self.left:
                self.left.buildTree(data)
            else:
                self.left = Node(data)
        
        # add node in right
        else:
            if self.right:
                self.right.buildTree(data)
            else:
                self.right = Node(data)

        
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)


s = Node(10)
s.buildTree(5)
s.buildTree(15)
s.buildTree(3)
s.buildTree(7)
s.buildTree(18)

s.inorder(s)

