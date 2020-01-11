"""Binary Search Tree implementation"""

class BinaryNode:

    def __init__(self, value = None):
        """Create Bianry Node"""
        self.value  =  value
        self.left = None
        self.right = None

    

class BinaryTree:

    def __init__(self):
        """Create empty binary tree"""
        self.root = None
    
    def add(self, value):
        """Insert value into proper location in Binary Tree"""
        