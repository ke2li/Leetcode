# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: 
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return root == None or self.rowSymmetric(root.left, root.right)
    
    def rowSymmetric(self, left, right):
        if left == None or right == None:
            return left==right
        if left.val != right.val:
            return False
        return self.rowSymmetric(left.left, right.right) and self.rowSymmetric(left.right, right.left)