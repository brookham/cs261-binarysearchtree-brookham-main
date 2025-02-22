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
        if self.key == key:
            return self
        elif key < self.key:
            if self.left != None:
                return self.left.search(key)
            else:
                return None
        else:
            if self.right != None:
                return self.right.search(key)
            else:
                return None
        
    def delete(self, key):
        node = self.search(key)
        if node == None:
            return self
        
        #deleting leaf node
        if node.left == None and node.right == None:
            if node.parent != None:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
            return self if node != self else None
        
        #deleting node with one child
        if node.left == None or node.right == None:
            if node.left:
                left_child = node.left
                left_child.parent = node.parent
                return left_child
            else:
                right_child = node.right
                right_child.parent = node.parent
                return right_child
        
        #two level node with two children
        if node.left and node.right:
            successor = node.right
            while successor.left:
                successor = successor.left
                # node = successor
                # node.right = node.right.delete(successor)
            node.key = successor.key
            successor = None
            return node
        

    def is_leaf(self):
        if self.left == None and self.right == None:
            return True
        
    def has_left_child(self):
        if self.left != None:
            return True
        
    def has_right_child(self):
        if self.right != None:
            return True
    
    def minimum(self):
        while self.left:
            self = self.left
        return self
    
    def pre_order(self):
        return self










