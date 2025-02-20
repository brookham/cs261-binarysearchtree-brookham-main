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

    def insert(self, child):
        if (child.key <= self.key) and (self.left == None):
            self.left = child
            
        
