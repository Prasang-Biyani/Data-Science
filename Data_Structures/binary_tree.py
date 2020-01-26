"""Binary Tree Implementation"""

class Binary_Node:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    

    def add(self, value):
        """Adds value to the binary node."""
        if self.value <= value:
            if self.left is None:
                self.left = Binary_Node(value)
            else:
                self.left.add(value)
        else:
            if self.right is None:
                self.right = Binary_Node(value)
            else:
                self.right.add(value)

    def delete(self):
        """Remove value of self from BinaryTree, works in 
        conjunction with remove method in BinaryTree"""

        if self.left == self.right == None:
            return None
        if self.left == None:
            return self.right
        if self.right == None:
            return self.left
        
        child = self.left
        grandchild = child.right
        if grandchild:
            while grandchild.right:
                child = grandchild
                grandchild = child.right
            self.value = grandchild.value
            child.right = grandchild.left
        else:
            self.left = child.left
            self.value = child.value
        return self

class Binary_Tree:

    def __init__(self):
        self.root = None

    def add(self, value):
        """Adds Value to the Binary Tree"""
        if self.root is None:
            self.root = Binary_Node(value)
        else:
            self.root.add(value)

    def contains(self, target) -> bool:
        """Checks whether the target value is present in BST."""
        node = self.root
        while node:
            if node.value == target:
                return True
            if node.value <= target:
                node = node.left
            else:
                node = node.right
        return False

    def removeFromParent(self, parent, value):
        """remove value from tree rooted at parent."""
        if parent is None:
            return None
        
        if value == parent.value:
            return parent.delete()
        elif value < parent.value:
            parent.left = self.removeFromParent(parent.left, value)
        else:
            parent.right = self.removeFromParent(parent.right, value)
        return parent

    def remove(self, value):
        """Remove value from tree."""
        if self.root:
            self.root = self.removeFromParent(self.root, value)




if __name__ == "__main__":
    bt = Binary_Tree()
    bt.add(5)
    bt.add(10)
    bt.add(4)
    bt.add(6)
    print(bt.contains(6))
    bt.remove(6)
    print(bt.contains(6))
