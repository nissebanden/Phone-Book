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
                return self.leftChild.Search(val)
            else:
                return None
        else:
            if self.rightChild:
                return self.rightChild.Search(val)
            else:
                return None
    def PrintTree(self):
        if self.leftChild:
            self.leftChild.PrintTree()
        print(self.data)
        if self.rightChild:
            self.rightChild.PrintTree()

def deleteNode(root, k):
    # Base case
    if root is None:
        return root

    # Recursive calls for ancestors of
    # node to be deleted
    if root.data > k:
        root.leftChild = deleteNode(root.leftChild, k)
        return root
    elif root.data < k:
        root.rightChild = deleteNode(root.rightChild, k)
        return root

    # We reach here when root is the node
    # to be deleted.

    # If one of the children is empty
    if root.leftChild is None:
        temp = root.rightChild
        del root
        return temp
    elif root.rightChild is None:
        temp = root.leftChild
        del root
        return temp

    # If both children exist
    else:

        succParent = root

        # Find successor
        succ = root.rightChild
        while succ.left is not None:
            succParent = succ
            succ = succ.leftChild

        # Delete successor.  Since successor
        # is always left child of its parent
        # we can safely make successor's right
        # right child as left of its parent.
        # If there is no succ, then assign
        # succ.right to succParent.right
        if succParent != root:
            succParent.leftChild = succ.rightChild
        else:
            succParent.rightChild = succ.rightChild

        # Copy Successor Data to root
        root.data = succ.data

        # Delete Successor and return root
        del succ
        return root
            
root = BST("Benjamin")

root.Insert("Sonny")
root.PrintTree()

root = deleteNode(root, root.Search("Sonny"))
root.PrintTree()