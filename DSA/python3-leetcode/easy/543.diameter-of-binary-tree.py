#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_lenght = 0
        def recurse(node:TreeNode) :
            nonlocal max_lenght
            if not node : return 0 
            lDepth = recurse(node.left)
            rDepth = recurse(node.right)
            max_lenght = max(max_lenght,lDepth + rDepth) 
            return 1 + max(lDepth,rDepth)
        recurse(root)
        return max_lenght
# @lc code=end

