#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recurse (node : TreeNode) :
            if not node : return (True,0) 
            recursel = recurse(node.left) 
            recurser = recurse(node.right) 
            if recursel[0] and recurser[0] :
                return (abs(recursel[1] - recurser[1]) < 2,1 + max(recurser[1],recursel[1]))
            return (False,-1)
        return recurse(root)[0]    


# @lc code=end

