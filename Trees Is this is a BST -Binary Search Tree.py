# Trees: Is this is a BST (Binary Search Tree)?
# These functions list only the balancing check, the creation of the tree is assumed
# Optimized

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def check_left_and_right_balance(leaf):
    # give a node and it'll return if it's balanced
    # and the min and the max value
    if ( (leaf.left == None) & (leaf.right == None)): 
        return 1, leaf.data, leaf.data
    else: 
        if ( (leaf.left == None) ^ (leaf.right == None)): 
            return 0
    if ((leaf.data > leaf.left.data) &
         (leaf.data < leaf.right.data)):
        # they exist and they are balanced
        left_bal, left_max, left_min = check_left_and_right_balance(leaf.left)
        right_bal, right_max, right_min = check_left_and_right_balance(leaf.right) 
        sub_tree_bal = ((left_bal & right_bal) & 
                        (left_max < leaf.data) & (right_min > leaf.data))
        sub_tree_max = right_max
        sub_tree_min = left_min
        return sub_tree_bal, sub_tree_max, sub_tree_min
    else:
        return 0, 0, 0

def check_binary_search_tree_(root):
    if (root== None):
        return 0
    else:
        tree_bal, tree_max, tree_min = check_left_and_right_balance(root) 
        if (tree_bal ):
            return 1
        else:
            return 0

