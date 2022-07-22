class BST:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left == None:
                    currentNode = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right == None:
                    currentNode = BST(value)
                    break
                else:
                    currentNode = currentNode.right

    def contains_or_search(self, value):
        pass

    def remove(self, value, Parent_Node=None):
        pass
