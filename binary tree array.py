class binarytree:
    def __init__(self,size):
        self.tree=[None]*size
        self.size=size
    def insert_root(self,data):
        self.tree[0]=data
    def set_right(self,i,data):
        child=2*i+2
        if child<self.size:
            self.tree[child]=data
        else:
            print("indeex out of range")
    def set_left(self,i,data):
        child=2*i+1
        if child<self.size:
            self.tree[child]=data
        else:
            print("index out of range")
    def preorder(self,i=0):
        if i>=self.size or self.tree[i] is None:
            return
        print(self.tree[i],end=" ")
        self.preorder(2*i+1)
        self.preorder(2*i+2)
        
        
    def inorder(self,i=0):
        if i>=self.size or self.tree[i] is None:
            return
        self.inorder(2*i+1)
        print(self.tree[i],end=" ")
        self.inorder(2*i+2)
    def postorder(self,i=0):
        if i>=self.size or self.tree[i] is None:
            return
        self.postorder(2*i+1)
        self.postorder(2*i+2)
        print(self.tree[i],end=" ")
    def levelorder(self):
        for value in self.tree:
            if value is not None:
                print(value,end=" ")
    def display(self):
        if self.tree[0] is None:
            print("no elements in tree")
        for i in range(self.size):
            print(f"index {i} :{self.tree[i]}")
tree=binarytree(7)
tree.insert_root('A')
tree.set_left(0,'B')
tree.set_right(0,'C')
print("\npreorder\n",end=" ")
tree.preorder()
print("\ninorder\n",end=" ")
tree.inorder()
print("\npostorder\n",end=" ")
tree.postorder()
print("\nlevel order\n",end=" ")
tree.levelorder()
print("\ndisplay\n",end=" ")
tree.display()
            
                
        
        
        
