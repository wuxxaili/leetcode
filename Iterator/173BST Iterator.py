# 173  Binary Search Tree Iterator
"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""
'''
Store the left side, pop and print it, then store the right side.
'''
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.parent = []
        self.cur = None
        self.flat(root)
        
    def flat(self,node):
        while node:
            self.parent.append(node)
            node = node.left
            
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.parent == []: 
            return False
        self.cur = self.parent.pop()
        self.flat(self.cur.right)
        return True

    def next(self):
        """
        :rtype: int
        """
        return self.cur.val
        
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())