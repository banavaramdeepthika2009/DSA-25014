class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class binarytree:
    def __init__(self):
        self.root=None
    def create(self):
        self.root=Node('A')
        self.root.left=Node('B')
        self.root.right=Node('c')
        self.root.left.left=Node('D')
        self.root.left.right=Node('E')
    def preorder(self,node):
        if node is None:
            return
        print(node.data,end=" ")
        self.preorder(node.left)
        self.preorder(node.right)
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data,end=" ")
        self.inorder(node.right)
    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data,end=" ")
    def levelorder(self):
        if self.root is  None:
            return
        
        queue=[self.root]
        while queue:
            node=queue.pop(0)
            print(node.data,end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                
                queue.append(node.right)
tree=binarytree()
tree.create()
print("\npreorder\n",end=" ")
tree.preorder(tree.root)
print("\ninorder\n",end=" ")
tree.inorder(tree.root)
print("\npostorder\n",end=" ")
tree.postorder(tree.root)
print("\nlevel order\n",end=" ")
tree.levelorder()

            
                
        
        
        
