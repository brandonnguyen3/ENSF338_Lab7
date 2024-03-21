#Exercise 1 (Complete)

import random
import time
import matplotlib.pyplot as plt
# Used chat gpt for some functions 
class Node:
    # Constructor \
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  #Initializes height to 1
 
#insert function
def insert(node, key):
    # If the tree is empty then return a new node
    if node is None:
        return Node(key)
 
    #Uses recursion
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node
 
    # Update the height of the current node
    node.height = 1 + max(get_height(node.left), get_height(node.right))
 
    return node
 
#Search function
def search(root, key):
    #Checks case that root is null or key is present at root
    if root is None or root.key == key:
        return root
 
    #Key is greater than the root value
    if root.key < key:
        return search(root.right, key)
 
    #Key is less than the root value
    return search(root.left, key)
 
#gets the height of a node. 
def get_height(node):
    if node is None:
        return 0
    return node.height
 
#Calculates the height. 
def get_balance(node):
    if node is None:
        return 0
    return get_height(node.right) - get_height(node.left)

#Used chatgpt to generate search tasks.  
#Function to generate random search tasks
def generate_search_tasks():
    tasks = []
    integers = list(range(1, 1001))  # First 1000 integers
    for _ in range(1000):
        random.shuffle(integers)
        tasks.append(integers.copy())
    return tasks
 
# Function to measure performance for each search task
def measure_performance(tasks):
    results = []
    for task in tasks:
        root = None
        for key in task:
            root = insert(root, key)
        
        search_times = []
        for key in task:
            start_time = time.time()
            search(root, key)
            end_time = time.time()
            search_times.append(end_time - start_time)
        
        avg_search_time = sum(search_times) / len(search_times)
        max_balance = max(abs(get_balance(root.left)), abs(get_balance(root.right)))
        results.append((max_balance, avg_search_time))
    
    return results
 
# Main function
if __name__ == "__main__":
    tasks = generate_search_tasks()
    results = measure_performance(tasks)
    
    # Extracting data for scatter plot
    abs_balances = [result[0] for result in results]
    search_times = [result[1] for result in results]
    
    # Scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(abs_balances, search_times, alpha=0.6)
    plt.xlabel('Absolute Balance')
    plt.ylabel('Search Time')
    plt.title('Absolute Balance vs. Search Time')
    plt.grid(True)
    plt.show()
