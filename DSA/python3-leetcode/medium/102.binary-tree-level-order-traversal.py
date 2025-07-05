#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root : return []
        res = []
        q = deque()
        q.append(root) 
        while q :
            temp = []
            for i in range(len(q)) :
                node = q.popleft()
                temp.append(node.val) 
                if node.left : q.append(node.left) 
                if node.right : q.append(node.right)
            res.append(temp)        
        return res

# @lc code=end

