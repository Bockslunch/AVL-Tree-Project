from avl import *

# Initialization:
avl_tree = AVLTree()

# Insertion:
avl_tree.insert_key(8)
avl_tree.insert_key(12)
avl_tree.insert_key(19)
avl_tree.insert_key(30)
avl_tree.insert_key(66)
avl_tree.insert_key(25)

# Printing
print("AVL tree inorder traversal:", end=" ")
avl_tree.print_tree()  # Output: 8 12 19 25 30 66

# Searching
search_result = avl_tree.search_key(19)
print("\nSearching for key 19:", search_result)  # Output: AVLNode object

# Deletion
avl_tree.delete_key(19)
print("AVL tree inorder traversal after deletion of key 19:", end=" ")
avl_tree.print_tree()  # Output: 8 12 25 30 66