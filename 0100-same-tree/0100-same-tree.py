# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        # Case 1: both are None
        if not p and not q:
            return True
        
        # Case 2: one is None, other is not
        if not p or not q:
            return False
        
        # Case 3: values differ
        if p.val != q.val:
            return False
        
        # Recursive check
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))

        