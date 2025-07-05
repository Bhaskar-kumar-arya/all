#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,left = None , right = None):
        self.val = x
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.val)   

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parentof = {root : None}
        def mapParents (node : TreeNode) :
            if not node : return 
            if node.left : 
                parentof[node.left] = node
                mapParents(node.left)
            if node.right : 
                parentof[node.right] = node
                mapParents(node.right)
        mapParents(root)    
        qParentlist = set()
        while q :
            qParentlist.add(q)
            q = parentof[q]
        while p :
            if p in qParentlist :
                return p
            p = parentof[p]
        
# @lc code=end
tree = TreeNode(1,TreeNode(2,TreeNode(4)),TreeNode(3))
print(Solution().lowestCommonAncestor(tree,tree.left.left,tree.right))