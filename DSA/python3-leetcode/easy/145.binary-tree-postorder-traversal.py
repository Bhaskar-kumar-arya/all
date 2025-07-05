#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        def recurse (node) :
            if not node : return
            recurse(node.left)
            recurse(node.right)
            res.append(node.val)
        recurse(root)
        return res    
# @lc code=end 

