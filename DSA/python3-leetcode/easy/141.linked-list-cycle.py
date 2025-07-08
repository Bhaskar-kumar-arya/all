#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next : ListNode = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        tortoise,hare = head,head
        while hare and hare.next :
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare : return True
        return False    
# @lc code=end  

