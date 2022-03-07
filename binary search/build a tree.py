class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def buildTree(self,data):
        if data == -1:
            return None
        
        Node(data)
        self.buildTree(self.left, data )
        self.buildTree(self.right, data)

    def preorder(self,root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)


s = Node(1)
s.buildTree(2)
s.buildTree(3)
s.buildTree(4)
s.buildTree(5)
s.buildTree(6)
s.preorder(s)

