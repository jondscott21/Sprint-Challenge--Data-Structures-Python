import sys
import random
# sys.path.append('./dll_stack')
# sys.path.append('./dll_queue')
# from dll_queue import Queue
# from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == None:
            self.value = value
            return self.value
        if self.value < value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                return self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # print(self.value, target)
        if self.value == target:
            return True
        if self.value > target:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif self.value < target:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
            

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)
        return

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            node.right.in_order_print(node.right)
        


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     queue = Queue()
    #     queue.enqueue(self)
    #     while queue.len() > 0:
    #         current_node = queue.dequeue()
    #         print(current_node.value)   
    #         if current_node.right:
    #             queue.enqueue(current_node.right)
    #         if current_node.left:
    #             queue.enqueue(current_node.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # def dft_print(self, node):
    #     stack = Stack()
    #     stack.push(self)
    #     while stack.len() > 0:
    #         current_node = stack.pop()
    #         print(current_node.value)   
    #         if current_node.right:
    #             stack.push(current_node.right)
    #         if current_node.left:
    #             stack.push(current_node.left)
    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left is not None:
            self.left.pre_order_dft(node.left)
        if node.right is not None:
            self.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left is not None:
            self.left.post_order_dft(node.left)
        if node.right is not None:
            self.right.post_order_dft(node.right)
        print(node.value)

# bst = BinarySearchTree(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst = BinarySearchTree('jerry')
# bst.insert('fred')
# bst.insert('tom')
# bst.insert('bob')
# bst.insert('angela')
# bst.insert('sam')
# bst.insert('jenny')
# bst.insert('ashley')

# bst.in_order_print(bst)
# print('******')
# bst.bft_print(bst)
# print('******')
# bst.pre_order_dft(bst)
# print('******')
# bst.post_order_dft(bst)

# def print_falsey(val):
#     if not val:
#         print('1st', True)
#     if val is None:
#         print('2nd',True)
# print_falsey(0)