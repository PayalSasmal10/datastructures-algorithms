"""
1. Binary tree can't have more than 2 nodes
2. can be formed like left part of root are small and right part of it are higher values.
3. They will be unique nodes like set 
4. max no of nodes in a binary tree with height 2^(no of level) - 1
5. perfect binary tree height with n nodes h = log(2)^(n+1) - 1
6. complete binary tree height with n nodes is h = log(2)^(n)
7. cost analysis is depend on height of a tree
8. Balanced Binary tree is differnces between height of left and right subtree for every node is not more than k ( mostly 1)
   diff = | hleft - hright |. for null leaf has -1 value
"""

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


    def buildTree(self,data):

        if data == self.data:
            return
        
        print("self.data = ", self.data)
        # add data in left node
        if data < self.data:
            print("self.left = ", self.left)
            if self.left:
                self.left.buildTree(data)
            else:
                self.left = Node(data)
        # add data in right node
        elif data> self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.buildTree(data)

        # self.root = Node(data)
        # self.left.buildTree(data)
        # self.right.buildTree(data)

    def preorder(self,root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)


s = Node(4)
s.buildTree(3)
s.buildTree(1)
s.buildTree(4)
s.buildTree(5)
s.buildTree(6)
s.preorder(s)

s.preorder()

