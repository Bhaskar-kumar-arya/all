#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        def __repr__ (self) :
            return self.val 
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root : return False 
        stack = [(root,root.val)]
        while stack :
            node,Currsum = stack.pop()
            if Currsum == targetSum and not node.left and not node.right : return True
            if node.left : stack.append((node.left,Currsum + node.left.val))
            if node.right : stack.append((node.right,Currsum + node.right.val)) 
        return False         

# @lc code=end

# [1,2,3]


# root = TreeNode(1, TreeNode(2), TreeNode(3))
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
print(Solution().hasPathSum(root,7))