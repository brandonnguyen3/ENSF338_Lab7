import sys 
sys.setrecursionlimit(10000)
from collections import deque

class Node:
    # Constructor
    def __init__(self, key, parent = None):
        self.key = key #value
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 1  # Initializes height to 1
        self.balance = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.pivot = None
    
    # search method 
    def search(self, key, root = None):
        if root is None:
            root = self.root
        current = root
        while current is not None:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return None

    # insertion method
    def insert(self, key):
        current = self.root
        parent = None

        while current is not None:
            parent = current
            if key <= current.key:
                current = current.left
            else:
                current = current.right

        newnode = Node(key, parent)    
        if parent is None:
            self.root = newnode
        elif key <= parent.key:
            parent.left = newnode
        else:
            parent.right = newnode
        
        self.updateHeight(newnode)
        self.updateBalance(newnode)

        return newnode

    def updateBalance(self, node):
        if node is None:
            return
        self.pivot = None
        pivotBalance = 0
        nodeInserted = node
        parent = node.parent

        while node is not None:
            if node.balance >= 1 or node.balance <= -1:
                if self.pivot is None:
                    self.pivot = node
                    pivotBalance = node.balance
            #update balance of the current node
            node.balance = self.getBalance(node)
            node = node.parent

        #check cases
        if self.pivot is None:
            print("Case #1: Pivot not detected")
        else:
            if pivotBalance >= 1:
                #if inserted node is in the right subtree
                if nodeInserted.key < self.pivot.key:
                    print("Case #2: A pivot exists and a node was added to the shorter subtree")
                else: 
                    #if inserted node is in the left subtree
                    #nodeInserted.key > self.pivot.key
                    print("Case #3: Not supported")
            elif pivotBalance <= -1:
                #if inserted node is in the right subtree
                if nodeInserted.key > self.pivot.key:
                    print("Case #2: A pivot exists and a node was added to the shorter subtree")
                else:
                    #nodeInserted.key < self.pivot.key
                    print("Case #3: Not supported for now")
       
      # get balance method
    def getBalance(self, node):
        if node is None:
            return 0
        return self.getHeight(node.right) - self.getHeight(node.left)
    
    # get height method
    def getHeight(self, node):
        if node is None:
            return 0
        return node.height
    
    def updateHeight(self, node):
        while node is not None:
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
            node = node.parent
        
    def printBalances(self):
        if self.root is None:
            return

        stack = deque()
        node = self.root

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print("Node:", node.key, "Balance:", node.balance)
                node = node.right
    


"""
Testing
Note: for every insertion it prints what case it falls into. 
We foucus on the last insertion for each test to check the case.
"""
      
# CASE ONE: No pivot               
def testOne():
    #case one 
    AVLTest = BinarySearchTree()
    AVLTest.insert(5) #case 1: no pivot
    AVLTest.insert(4) #Case 1 - No pivot
    AVLTest.insert(6) #Case 2: 
    #after inserting 7, it should print "Case 1: Pivot not detected"
    AVLTest.insert(7) #Case 1
    print("Balances for each node:")
    AVLTest.printBalances()

#CASE TWO: A pivot exists, and a node was added to the shorter subtree
def testTwo():
    #case two
    AVLTest = BinarySearchTree()
    AVLTest.insert(5) #case 1: no pivot
    AVLTest.insert(4) #Case 1 - No pivot
    AVLTest.insert(6) #Case 2: 
    AVLTest.insert(7) #Case 1
    #after inserting 3, it should print "Case 2: A pivot exists and a node was added to the shorter subtree"
    AVLTest.insert(3) #Case 2: 
    print("Balances for each node:")
    AVLTest.printBalances()

#CASE THREE: Not supported
def testThree():
    AVLTest = BinarySearchTree()
    AVLTest.insert(60) 
    AVLTest.insert(40) 
    AVLTest.insert(80) 
    AVLTest.insert(20) 
    AVLTest.insert(50) 
    AVLTest.insert(95) 
    AVLTest.insert(10) 
    AVLTest.insert(30) 
    #after inserting 8, it should print "Case 3: Not supported"
    AVLTest.insert(8) 

testOne()
print("end of test one")
testTwo()
print("end of test two")
testThree()




"""
# Example usage:
bst = BinarySearchTree()
keys = [5, 4, 6, 7, 3]

# Insert keys into the BST
for key in keys:
    bst.insert(key)
# • Adding a node results in case 3 (the code should print “Case 3 not supported”):
bst1 = BinarySearchTree()
#keys = [5, 4, 6, 7, 3]
keys = [60, 40, 80, 20, 50, 95, 10, 30, 5]

#Insert keys into the BST
for key in keys:
    bst1.insert(key)

print("Balances for each node:")
bst.print_balances()
"""



