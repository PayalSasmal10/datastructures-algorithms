class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def buildTree(self, data):

        if data == self.data:
            return 

        # if data < self.data

        if data < self.data:
            if self.left:
                self.left.buildTree(data)
            else:
                self.left = Node(data)

        else:

            if self.right:
                self.right.buildTree(data)
            else:
                self.right = Node(data)

    
    def preorder(self, root):
        if root:
            print(root.data, "->", end="")
            self.preorder(root.left)
            self.preorder(root.right)

    def height(self, root):
        if root == None:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)

        return 1+max(lh,rh)
        


s = Node(4)
s.buildTree(3)
#print(s.buildTree(3))
s.buildTree(1)
s.buildTree(4)
s.buildTree(5)
# s.buildTree(6)
s.preorder(s)
print("end")
print(s.height(s))