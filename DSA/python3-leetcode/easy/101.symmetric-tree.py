#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root : return True
        lstack = [root.left]
        rstack = [root.right]
        while lstack and rstack :
            lnode = lstack.pop()
            rnode = rstack.pop()
            if not lnode and not rnode : continue
            if not lnode or not rnode : return False
            if not lnode.val == rnode.val  : return False
            lstack.append(lnode.left) 
            rstack.append(rnode.right)    
            lstack.append(lnode.right) 
            rstack.append(rnode.left) 
        return True    


# @lc code=end

