#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root : return 0
        maxDepth = 1
        stack = [(root,1)] 
        while stack :
            node,currDepth = stack.pop()
            if node.right :
                stack.append((node.right,currDepth + 1)) 
            if node.left :
                stack.append((node.left,currDepth + 1))    
            if node.right or node.left :
                maxDepth = max(currDepth + 1,maxDepth)
        return maxDepth            


# @lc code=end

