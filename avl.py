# Creating node class with key, left and right 
# children, and height of itself (1)
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Creating Tree class with main functions and helper functions
class AVLTree:
    def __init__(self):
        self.root = None

    # returns a node's height for use in keeping balance
    def height(self, node):
        if node is None:
            return 0
        return node.height

    # calls height() function and returns difference 
    # between left/right children
    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    # right rotation function for re-balancing tree 
    # during insertion/deletion
    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        # finds larger of left/right child heights and 
        # adds 1 for the root (x/y) node of that branch
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    # right rotation function for re-balancing tree 
    # during insertion/deletion
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        # finds larger of left/right child heights and 
        # adds 1 to set height of newly-balanced nodes
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    # insertion function to create a new node in AVL tree
    # includes balancing operations to ensure branch heights never
    # differ by more than 1
    def insert(self, node, key):
        if node is None:
            return AVLNode(key)
        
        # recursive calls to traverse tree and find 
        # correct insertion location
        if key < node.key:
            node.left = self.insert(node.left, key) 
        else:
            node.right = self.insert(node.right, key)
        
        # sets height of newly inserted node
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # sets balance variable by calling balance factor function
        # to find difference in the heights of branches
        balance = self.balance_factor(node)

        # uses balance variable to determine which rotations (left/right) 
        #to make for rebalancing
        if balance > 1:  # left branch/tree has larger height than right
            if key < node.left.key:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
        
        if balance < -1:  # right branch/tree has larger height than left
            if key > node.right.key:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
        
        return node

    def delete(self, root, key):
        if root is None: # base case for empty tree
            return root
        
        # recursive calls to traverse tree and find key of
        # node to be deleted
        if key < root.key:
            root.left = self.delete(root.left, key) #traverse left
        elif key > root.key:
            root.right = self.delete(root.right, key) #traverse right
        else:  # if current node is the one to be deleted
            if root.left is None:
                temp = root.right
                root = None # deleting node
                return temp # right child is new root of subtree
            elif root.right is None:
                temp = root.left
                root = None # deleting node
                return temp # left child is new root of subtree

            # find successor
            temp = self.min_value_node(root.right)
            # copy successor key to current node
            root.key = temp.key 
            # delete successor
            root.right = self.delete(root.right, temp.key)
        
        # balancing operations like those of Insertion function
        # using root instead of node
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        
        balance = self.balance_factor(root)
        
        if balance > 1:
            if self.balance_factor(root.left) >= 0:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        
        if balance < -1:
            if self.balance_factor(root.right) <= 0:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
        
        return root        

    # helper function to find node with min value
    def min_value_node(self, node):
        current = node
        # traverse to find leaf furthest to left (min value)
        while current.left is not None:
            current = current.left
        return current

    # calls insert function and updates the root    
    def insert_key(self, key):
        self.root = self.insert(self.root, key)
    
    # calls delete function and updates the root
    def delete_key(self, key):
        self.root = self.delete(self.root, key)

    # recursively searches for key and returns node if found
    # returns None if key not found
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)
    
    # calls search function with root node
    def search_key(self, key):
        return self.search(self.root, key)

    # recursively traverse tree and prints keys in order
    def inorder_traversal(self, node):
        if node: 
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

    # calls inorder traversal to print keys of tree in order
    def print_tree(self):
        self.inorder_traversal(self.root)
