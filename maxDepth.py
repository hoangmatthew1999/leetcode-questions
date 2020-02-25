class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
    def invertTree(self):
        temp = self.right.data
        print(temp)
        self.right.data = self.left.data
        print(self.right.data)
        self.left.data = temp
        print(self.left.data)

        self = self.left
        print(self.left.data, "left")
        print(self.right.data,"right")


# Use the insert method to add nodes
root = Node(4)
root.insert(2)
root.insert(7)
root.insert(1)
root.insert(3)
root.insert(6)
root.insert(9)


root.PrintTree()
root.invertTree()
root.PrintTree()
