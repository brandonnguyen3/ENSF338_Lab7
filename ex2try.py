import random
import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.balance = 0  # Added balance attribute to the node

class BSearchTree:
    def __init__(self):
        self.root = None

    def process(self, key, search=False):
        if search:
            return self.search(self.root, key)
        else:
            self.root = self.insert(self.root, key)
            return None

    def insert(self, node, key):
        if node is None:
            return Node(key)
        
        if key < node.key:
            node.left = self.insert(node.left, key)
            node.balance -= 1  # Update balance when inserting into the left subtree
        elif key > node.key:
            node.right = self.insert(node.right, key)
            node.balance += 1  # Update balance when inserting into the right subtree
        
        # Check for Case 1: Pivot does not exist
        assert abs(node.balance) <= 1, f"Case #1: Pivot not detected. Node {node.key} balance: {node.balance}"
        
        return self.rebalance(node)

    def rebalance(self, node):
        if abs(node.balance) <= 1:
            return node

        # Check for Case 2: Pivot exists but node is being inserted into the shorter subtree
        if node.balance < 0:
            assert node.balance >= -1, f"Case #2: A pivot exists, and a node was added to the shorter subtree. Node {node.key} balance: {node.balance}"
            return node

        # Case 3 not supported
        assert False, "Case #3 not supported"
    
    def search(self, node, key):
        if node is None or node.key == key:
            return node is not None
        
        if key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)
    
    def measure_balance(self):
        return self.measure_balance_recursive(self.root)
    
    def measure_balance_recursive(self, node):
        if node is None:
            return 0
        
        left_height = self.measure_balance_recursive(node.left)
        right_height = self.measure_balance_recursive(node.right)
        
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
    bst = BSearchTree()

    # Test Case 1: Adding a node results in Case 1 (pivot does not exist)
    bst.process(10)
    bst.process(5)
    bst.process(15)
    bst.process(3)

    # Test Case 2: Adding a node results in Case 2 (a pivot exists)
    bst.process(20)
    bst.process(25)
    bst.process(30)
    bst.process(35)
    bst.process(40)

    # Test Case 3: Adding a node results in Case 3 (not supported)
    try:
        bst.process(50)
    except AssertionError as e:
        assert str(e) == "Case #3 not supported", f"Unexpected error: {e}"

    # Test Case 4: Adding a node does not result in any case
    bst.process(2)

    tasks = generate_search_tasks()
    search_times, max_balances = measure_performance(bst, tasks)

    plt.scatter(max_balances, search_times, alpha=0.5)
    plt.title('Scatterplot of Absolute Balance vs. Search Time')
    plt.xlabel('Absolute Balance')
    plt.ylabel('Search Time (seconds)')
    plt.show()

