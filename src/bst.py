
class BTNode:
    '''Binary Tree Node class - do not modify'''

    def __init__(self, value, left, right):
        '''Stores a reference to the value, left child node, and right child node. If no left or right child, attributes should be None.'''
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        # reference to root node - do not modify
        self.root = None

    def insert(self, value):
        '''Takes a numeric value as argument.
        Inserts value into tree, maintaining correct ordering.
        Returns nothing.'''
        if self.root is None:
            self.root = BTNode(value, None, None)
            return
        self.insert2(self.root, value)
        
        
    def insert2(self, node, value):
        
        if value < node.value:
            if node.left is None:
                node.left = BTNode(value, None, None)
                return
            self.insert2(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = BTNode(value, None, None)
                return
            self.insert2(node.right, value)
        else:
            return 
            
            
        
    def search(self, value):
        '''Takes a numeric value as argument.
        Returns True if its in the tree, false otherwise.'''
        return self.search2(self.root, value)
  
    
    def search2(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self.search2(node.left, value)
        else:
            return self.search2(node.right, value)
        
        
    def height(self):
        '''Returns the height of the tree.
        A tree with 0 or 1 nodes has a height of 0.'''
        return self.height2(self.root) - 1

    
    def height2(self, node):
        if node is None:
            return 0
        return max(self.height2(node.left), self.height2(node.right)) + 1

    
    def preorder(self):
        '''Returns a list of the values in the tree,
        in pre-order order.'''
        return self.preorder2(self.root, [])


    def preorder2(self, node, lst):
        if node is not None:
            lst.append(node.value)
            self.preorder2(node.left, lst)
            self.preorder2(node.right, lst)
        return lst



#bst = BST()

#for value in [4, 2, 5, 3, 1, 6, 7]:
#    bst.insert(value)

## BST now looks like this:
##      4
##    /   \
##   2     5
##  / \     \
## 1   3     6
##            \
##             7

#print(bst.search(5))  # True
#print(bst.search(8))  # False
#print(bst.preorder())  # [4, 2, 1, 3, 5, 6, 7]
#print(bst.height())  # 3
