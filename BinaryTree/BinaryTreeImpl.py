class BT:
    def __init__(self,root):
        self.left = None
        self.right = None
        self.root = root
        self.c = 0
    
    def insert(self,root):
        if self.root:
            if root < self.root:
                if self.left is None:
                    self.left = BT(root)
                else:
                    self.left.insert(root)
            if root > self.root:
                if self.root is None:
                    self.root = BT(root)
                else:
                    self.right.insert(root)
        else:
            self.root=root

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.root, end=' ')
        if self.right:
            self.right.printTree()

    def findVal(self,val):
        if self.root==val:
            return str(val)+" found"
        elif val < self.root:
            if self.left is None:
                return "Val not found"
            else:
                return self.left.findVal(val)
        elif val > self.root:
            if self.right is None:
                return "Val not found"
            else:
                return self.right.findVal(val)
    
    def leftheight(self):
        if self.root==None:
            return self.c
        elif self.root:
                self.c+=1
                if self.left:
                    self.c+=1
                    return self.left.leftheight()
                else:
                    return self.c

    def rightheight(self):
        if self.root==None:
            return self.c
        elif self.root:
                self.c+=1
                if self.right:
                    self.c+=1
                    return self.right.rightheight()
                else:
                    return self.c

if __name__ == "__main__":
    node = BT(12)
    node.insert(6)
    node.insert(14)
    #node.insert(3)
    print(node.findVal(7))
    print(node.findVal(6))
    print(node.rightheight())
    node.printTree()
    print(node.leftheight())