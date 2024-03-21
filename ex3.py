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
        #self.updateBalanceAfterInsertion(newnode)

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
            node = node.parent

        # Update balance of the current node
        node = nodeInserted
        while node is not None:
            node.balance = self.getBalance(node)
            node = node.parent

        # Check cases
        if self.pivot is None:
            print("Case #1: Pivot not detected")
        else:
            if pivotBalance >= 1:
                # If inserted node is in the right subtree
                if nodeInserted.key < self.pivot.key:
                    print("Case #2: A pivot exists and a node was added to the shorter subtree")
                elif nodeInserted.key > self.pivot.key:
                    # If inserted node is in the left subtree
                    if nodeInserted.key > nodeInserted.parent.key:
                        print("Case #3a: adding a node to an outside subtree")
                        self.leftRotate(self.pivot)
                    elif nodeInserted.key < nodeInserted.parent.key:
                        print("Case #3b: Not supported for now")
            
            elif pivotBalance <= -1:
                # If inserted node is in the right subtree
                if nodeInserted.key > self.pivot.key:
                    print("Case #2: A pivot exists and a node was added to the shorter subtree")
                elif nodeInserted.key < self.pivot.key:
                    # If inserted node is in the left subtree
                    if nodeInserted.key < nodeInserted.parent.key:
                        print("Case #3a: adding a node to an outside subtree")
                        self.rightRotate(parent)
                    elif nodeInserted.key > nodeInserted.parent.key:
                        print("Case #3b: Not supported for now")

    def updateHeight(self, node):
        while node is not None:
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
            node = node.parent

       
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
    
    
    # Internal method for left rotation
    #used chatgpt
    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        # Update heights after rotation
        self.updateHeight(x)
        self.updateHeight(y)
        # Update balance factors after rotation
        self.updateBalance(x)
        self.updateBalance(y)

    # Internal method for right rotation
    def rightRotate(self, y):
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y is y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
        # Update heights after rotation
        self.updateHeight(y)
        self.updateHeight(x)
        # Update balance factors after rotation
        self.updateBalance(y)
        self.updateBalance(x)

  
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
    #end of chatgpt code
    


"""
Testing
Note: for every insertion it prints what case it falls into. 
We foucus on the last insertion for each test to check the case.
"""

# Testing
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

def testTwo():
    #case two
    AVLTest = BinarySearchTree()
    AVLTest.insert(5) #case 1: no pivot
    AVLTest.insert(4) #Case 1 - No pivot
    AVLTest.insert(6) #Case 2: 
    AVLTest.insert(7) #Case 1
    #after inserting 3, it should print "Case 2: A pivot exists and a node was added to the shorter subtree"
    AVLTest.insert(3) #Case 2: 
    #print("Balances for each node:")
    #AVLTest.printBalances()

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
    #after inserting 8, it should print "Case 3a:"
    AVLTest.insert(8) 
    #print("Balances for each node:")
    #AVLTest.printBalances()

def testFour():
    AVLTest = BinarySearchTree()
    AVLTest.insert(100) 
    AVLTest.insert(40) 
    AVLTest.insert(80) 
    AVLTest.insert(50) 
    AVLTest.insert(90) 
    #after inserting 45, it should print "Case 3b: Not supported"
    AVLTest.insert(45) 

testOne()
print("end of test one")
print("\n")
testTwo()
print("end of test two")
print("\n" )
testThree()
print("end of test three")
print("\n")
testFour()