import random
import timeit
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(20000)

# Tree node definition
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.height = 1  # Initialize height to 1

class BSearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        current = self.root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        new_node = Node(data, parent)

        if data <= parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        # Update heights after insertion
        self.update_height(new_node)
        
        # Identify pivot node
        pivot_node = self.find_pivot_node(new_node)

        # Check for cases
        if pivot_node is None:
            print("Case #1: Pivot not detected")
            self.update_balances(new_node)
        else:
            if self.is_shorter_subtree(new_node, pivot_node):
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
                self.update_balances(new_node)

        #print(f"Balance of Node {data}: {self.get_balance(new_node)}")

    def find_pivot_node(self, node):
        while node:
            balance = self.get_balance(node)
            if balance != 0:
                return node
            node = node.parent
        return None

    def is_shorter_subtree(self, node, pivot):
        if pivot is None:
            return False
        pivot_balance = self.get_balance(pivot)
        if pivot_balance == 0:
            return False
        if node.data <= pivot.data:
            return pivot_balance < 0
        else:
            return pivot_balance > 0

    def update_balances(self, node):
        while node:
            node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
            node = node.parent

    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return current
            elif data <= current.data:
                current = current.left
            else:
                current = current.right
        return None

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        while node:
            node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
            node = node.parent

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def findMaxBalance(self, node):
        if not node:
            return 0
        return max(self.get_balance(node), self.findMaxBalance(node.left), self.findMaxBalance(node.right))



# Test Case 1: (Pivot not detected)
def test_case_1():
    bst = BSearchTree()
    for data in [50, 30, 70]:
        bst.insert(data)
    bst.insert(80)

# Call the test case function
test_case_1()



