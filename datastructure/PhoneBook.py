
class BST:
    def __init__(self, data):
        self.leftChild = None
        self.rightChild = None
        self.data = data

    def Insert(self,data):
        if data < self.data:
            if self.leftChild:
                self.leftChild.insert(data)
            else:
                self.leftChild = BST(data)
                return
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = BST(data)
                return
            
    def Search(self,val):
        if val==self.data:
            return val
        elif val < self.data:
            if self.leftChild:
                return self.leftChild.search(val)
            else:
                return None
        else:
            if self.rightChild:
                return self.rightChild.search(val)
            else:
                return None
    
    def PrintTree(self):
        if self.leftChild:
            self.leftChild.PrintTree()
        print(self.data)
        if self.rightChild:
            self.rightChild.PrintTree()
            
root = BST("Benjamin")

root.Insert("Sonny")
root.PrintTree()
