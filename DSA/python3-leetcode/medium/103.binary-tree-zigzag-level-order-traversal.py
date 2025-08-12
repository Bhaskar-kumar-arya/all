#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root : return
        res = []
        stack =[root]
        dir = 1
        while stack :
            path = []
            for i in range(len(stack)) :
                node = stack.pop()
                path.append(node.val)
                if node.right :  stack.append(node.right)
                if node.left : stack.append(node.left)
            res.append(path)  
            dir *= -1  
        return res    

        
# @lc code=end

