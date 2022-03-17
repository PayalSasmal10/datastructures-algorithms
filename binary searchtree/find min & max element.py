
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def buildTree(self, data):
        if self.data == data:
            return
        
        elif data < self.data:
            if self.left:
                self.left.buildTree(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.buildTree(data)
            else:
                self.right = Node(data)

    def findMin(self,root):
        if root:
            if root.left == None:
                print(root.data)
            self.findMin(root.left)

    def findMax(self, root):
        if root:
            if root.right == None:
                print(root.data)
            self.findMax(root.right)


s = Node(4)
s.buildTree(2)
s.buildTree(1)
s.buildTree(3)
s.buildTree(6)
s.buildTree(5)
s.findMin(s)
s.findMax(s)

