class BST:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None 

    def addNode(self, data):
        if self.data == data:
            return 

        if data < self.data:
            if self.left:
                self.left.addNode(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.addNode(data)
            else:
                self.right = BST(data)


    def search(self, data):
        if self.data == data: return True 

        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False 
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False 

            
    def InorderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.InorderTraversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.InorderTraversal()
        return elements


def BuildTree(elem):
    bst = BST(elem[0])
    for x in range(1, len(elem)):
        bst.addNode(elem[x])
    return bst

    


if __name__ == "__main__":
    elem = [17,16,5,2,1,90,66,77]
    bst = BuildTree(elem)
    print(bst.InorderTraversal())
    