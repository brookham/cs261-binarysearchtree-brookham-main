# BinarySearchTree: A binary search tree.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_bst.py.

# Name:
# Collaborators:
# Time spent:


class BinarySearchTree:
    def __init__(self, key = None):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key

    def insert(self, node):
        if (node.key <= self.key):
            if (self.left == None):
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        else: 
            if (self.right == None):
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)

    def search(self, key):
        if self.key != key:
            return None
        elif self.key == key:
            return self
        elif key < self.key:
            return self.search(key, self.left)
        else:
            return self.search(key, self.right)
        
    def delete(self, key):
        if self.search(key) == None:
            return self
        elif self.search(key) == self:
            return self.parent

    



            
        
