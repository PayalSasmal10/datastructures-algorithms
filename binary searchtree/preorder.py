# Binary search pre order trvaversal works like -> Root - Left - Right

class BuildTree:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
    
    def buildTree(self,data):
        if data == self.val:
            return
        
        # add in left
        if data < self.val:
            if self.left:
                self.left.buildTree(data)
            else:
                self.left = BuildTree(data)
        
        # add in right
        else:
            if self.right:
                self.right.buildTree(data)
            else:
                self.right = BuildTree(data)

    def preorder(self,root):
        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)




tree = BuildTree(15)
tree.buildTree(10)
tree.buildTree(20)
tree.buildTree(30)
tree.buildTree(15)
tree.preorder(tree)






