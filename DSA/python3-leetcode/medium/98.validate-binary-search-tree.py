#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        curr = root
        stack = []
        prev = None
        while stack or curr :
            while curr :
                stack.append(curr)
                curr = curr.left
            node : TreeNode = stack.pop()
            if prev and node.val <= prev.val : return False
            prev = node
            curr = node.right
        return True   

        
# @lc code=end




print(Solution().isValidBST(TreeNode(2,TreeNode(1),TreeNode(3))))