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

        newnode = Node(data, parent)

        if data <= parent.data:
            parent.left = newnode
        else:
            parent.right = newnode

        self.update_height(newnode)  # Update heights after insertion

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




# Generate the list of the first 1000 integers
integersList ={i for i in range(1, 1001)}
shuffleList = random.shuffle(integersList)

