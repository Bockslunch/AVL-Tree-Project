1. AVLNode Class: Defines a class representing a node in an AVL tree. Each node has a key value, left and right children, and a height attribute initialized to 1.

2. AVLTree Class: Defines a class representing the AVL tree itself. It includes various methods for insertion, deletion, searching, and traversal of the tree.

3. Initialization: The __init__ method initializes an empty AVL tree with a None root.

4. Height and Balance Factor: The height method calculates the height of a given node, while the balance_factor method calculates the balance factor of a node, which is the difference in height between its left and right subtrees.

5. Rotation Methods: Two rotation methods (rotate_right and rotate_left) are defined for rebalancing the tree during insertion and deletion operations.

6. Insertion: The insert method inserts a new key into the AVL tree while maintaining balance. It recursively traverses the tree to find the correct insertion location, updates node heights, and performs rotations if necessary to ensure the balance property of the AVL tree.

7. Deletion: The delete method deletes a node with a specified key from the AVL tree while maintaining balance. It recursively searches for the node to be deleted, handles different cases (node has no children, node has one child, node has two children), updates node heights, and performs rotations as needed to rebalance the tree.

8. Helper Functions: The min_value_node function finds the node with the minimum key value in a subtree, and the search function searches for a key in the AVL tree recursively.

9. Key Insertion and Deletion: The insert_key and delete_key methods are provided for inserting and deleting keys in the AVL tree. They call the respective insertion and deletion methods while updating the root of the tree.

10. Search and Traversal: The search_key method searches for a key in the AVL tree, and the print_tree method performs an in-order traversal of the tree to print its keys in sorted order.
