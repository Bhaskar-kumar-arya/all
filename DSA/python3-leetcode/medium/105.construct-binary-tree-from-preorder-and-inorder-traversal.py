#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode: 
            if not preorder : return None
            currIndex = inorder.index(preorder[-1]) 
            curr = TreeNode(preorder[0])
            curr.left = self.buildTree(preorder[1:currIndex],inorder[:currIndex])
            curr.right = self.buildTree(preorder[currIndex :],inorder[currIndex + 1 : ])
            return curr.val
# @lc code=end

print(Solution().buildTree([3,9,20],[9,3,20]))