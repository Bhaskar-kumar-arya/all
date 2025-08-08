#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        _k = 0
        curr = root
        stack =[]
        while stack or curr :
            while curr :
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            _k += 1
            if _k == k : return node.val
            curr = node.right


        
# @lc code=end

