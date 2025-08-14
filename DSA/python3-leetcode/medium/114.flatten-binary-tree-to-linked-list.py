    #
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        stack = []
        curr = root
        prev = None
        while stack or curr : 
            while curr : 
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            if prev : 
                prev.right = node
            prev = node
            curr = node.right    
           
# @lc code=end

root = (Solution().flatten(TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,None,TreeNode(6)))))

while root : 
    print(root.val)
    root = root.right