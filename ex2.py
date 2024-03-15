import random
import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BSearchTree:
    def __init__(self):
        self.root = None

    def process(self, key, search=False):
        if search:
            return self.search(self.root, key)
        else:
            self.root = self.recurisve(self.root, key)
            return None

    def insert(self, node, key):
        if node is None:
            return Node(key)
        
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)

        pivotNnode = self.identify_pivot(node)
        if not pivotNode:
            print("Case 1: Pivot not detected")
        else:

            print("Case 2: Pivot detected and a anode was added to the shorter subtree")

        return node

    def search(self, node, key):
        if node is None or node.key == key:
            return node is not None
        
        if key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)
    
    #used chatgpt for these two fucntions
    def measure_balance(self):
        return self.measure_balance_recursive(self.root)
    
    def measure_balance_recursive(self, node):
        if node is None:
            return 0
        
        left_height = self.measure_balance_recursive(node.left)
        right_height = self.measure_balance_recursive(node.right)
        
        return abs(left_height - right_height)
    
    def identify_pivot(self, node):
        left_height = self.measure_balance_recursive(node.left)
        right_height = self.measure_balance_recursive(node.right)
        if abs(left_height - right_height) > 1:
            return node
        else:
            return None


def generate_search_tasks():
    tasks = []
    integers = list(range(1, 1001))
    for _ in range(1000):
        random.shuffle(integers)
        tasks.append(integers.copy())
    return tasks



def measure_performance(tree, tasks):
    search_times = []
    max_balances = []
    for task in tasks:
        start_time = time.time()
        for integer in task:
            tree.process(integer, search=True)
        end_time = time.time()
        search_time = end_time - start_time
        balance = tree.measure_balance()
        search_times.append(search_time)
        max_balances.append(balance)
    return search_times, max_balances

if __name__ == "__main__":
    bst = BSearchTree()
    tasks = generate_search_tasks()
    search_times, max_balances = measure_performance(bst, tasks)

    plt.scatter(max_balances, search_times, alpha=0.5)
    plt.title('Scatterplot of Absolute Balance vs. Search Time')
    plt.xlabel('Absolute Balance')
    plt.ylabel('Search Time (seconds)')
    plt.show()

