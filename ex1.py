import random
import time
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def process(self, key, search=False):
        if search:
            return self._search_recursive(self.root, key)
        else:
            self.root = self._insert_recursive(self.root, key)
            return None

    def _insert_recursive(self, node, key):
        if node is None:
            return TreeNode(key)
        
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        
        return node

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node is not None
        
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
    
    def measure_balance(self):
        return self._measure_balance_recursive(self.root)
    
    def _measure_balance_recursive(self, node):
        if node is None:
            return 0
        
        left_height = self._measure_balance_recursive(node.left)
        right_height = self._measure_balance_recursive(node.right)
        
        return abs(left_height - right_height)


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
    bst = BinarySearchTree()
    tasks = generate_search_tasks()
    search_times, max_balances = measure_performance(bst, tasks)

    # Plotting
    plt.scatter(max_balances, search_times, alpha=0.5)
    plt.title('Scatterplot of Absolute Balance vs. Search Time')
    plt.xlabel('Absolute Balance')
    plt.ylabel('Search Time (seconds)')
    plt.show()
