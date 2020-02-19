import sys
sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

    # Insert the given value into the tree
    def insert(self, value):
        if not self.value:
            self.value = BinarySearchTree(value)
        if value is self.value:
            #  self.value = BinarySearchTree(value)
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        # item = BinarySearchTree.value.contains(value)
        elif value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        
        else: #value >= self.left: #value >= node go right
            if not self.right:
                self.right = BinarySearchTree(value)
        
            else:
                self.right.insert(value)
        
        
        # if self.right is None and self.left is None:
        #     return self.storage.enqueue(value)
        # if value > self.storage:
        #     self.right.enqueue(value)
        #     return
        # elif value < self.storage:
        #     self.left.enqueue(value)
        #     return
    

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        elif target >= self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        elif target != self.value:
            return False
    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()
           
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # if self.value:
        #     cb(self)
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
            # BinarySearchTree(self.left).for_each(cb)
        if self.right:
            # BinarySearchTree(self.right).for_each(cb)
             self.right.for_each(cb)
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        print(self.value)
        if self.left:
            self.left.in_order_print(node)
    
        if self.right:
            self.right.in_order_print(node)
    

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        print(self.value)
        if self.left:
            return self.left.bft_print(node)
    
        return self.right.bft_print(node)
        
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(self.value.for_each(node))
        if self.left:
           return self.left.dft_print(node)
    
        if self.right:
            return self.right.dft_print(node)
    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
