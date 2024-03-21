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
integersList = list(range(1, 1001))

# Generate 1000 different tasks by shuffling the list 1000 times
search_tasks = []
for _ in range(1000):
    shuffled_list = list(integersList)  
    random.shuffle(shuffled_list)
    search_tasks.append(shuffled_list)


avgPerformance = []
largestBalance = []

# Create an instance of Binary Search Tree
bst = BSearchTree()

# Measure performance for each task
for task in search_tasks:
    # Insert integers into the tree
    for integer in task:
        bst.insert(integer)
    
    # Measure search performance using timeit
    search_time = timeit.timeit(lambda: [bst.search(integer) for integer in task], number=1)

    # Measure largest absolute balance value
    largest_balance = bst.findMaxBalance(bst.root)

    # Append performance metrics to the respective lists
    avgPerformance.append(search_time / len(task))
    largestBalance.append(largest_balance)

# Plot scatterplot
plt.scatter(largestBalance, avgPerformance, alpha=0.5)
plt.title('Scatterplot of Absolute Balance vs. Average Search Time')
plt.xlabel('Largest Absolute Balance')
plt.ylabel('Average Search Time (seconds)')
plt.show()

