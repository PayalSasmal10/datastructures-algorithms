from datetime import date


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


s = Node(30)
s.buildTree(25)
s.buildTree(50)
s.buildTree(45)
s.buildTree(76)

s.inorder(s)

