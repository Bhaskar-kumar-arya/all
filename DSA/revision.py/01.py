# Example 2:

# Input: s = "()[]{}"

# Output: true
def validParenthisis(s : str) :
    stack = [s[0]]
    LeftToRight = {
        "{" : "}" ,
        "[" : "]" ,
        "(" : ")"
    }
    if s[0] not in LeftToRight : return False
    for i in range(1,len(s)) :
        print(f"{s[i]} , {stack}")
        if s[i] in LeftToRight.keys() : 
            stack.append(s[i])
        elif stack and LeftToRight[stack[-1]] == s[i] : 
            stack.pop()  
        else : return False
    print(f"{stack}")       
    return stack == []

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Input: list1 = [1,2,4], list2 = [2,3,4]
# Output: [1,2,2,3,4,4]

def mergeTwoLists(list1 : ListNode, list2 : ListNode) -> ListNode :  
    curr = ListNode()
    head = curr
    while list1 and list2 :
        if list1.val < list2.val :
            curr.next = list1
            list1 = list1.next
        else :
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    curr.next = list1 if list1 else list2           
    return head.next

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

def removeDuplicates(nums: list[int]) -> int:  
    j = 0
    for i in range(0,len(nums)) :
        if nums[i] != nums[j] :
            j += 1
            nums[j] = nums[i]
    return j + 1

# 1221
def isPalindrome(num : int) -> bool :
    if num < 0 or (num%10 == 0 and num != 0) : return False
    curr = 0
    while num > curr :
        curr = curr*10 + num%10 
        num = num // 10
    return num == curr or curr//10 == num

def longestCommonPrefix_vertical(strs : list[str]) -> str :
    minLen = min(len(s) for s in strs)
    for i in range(0,minLen)  :
        if not all(strs[0][i] == s[i] for s in strs) : return strs[0][:i]
    return strs[0][0:minLen]  

def longestCommonPrefix_horizontal (strs : list[str]) -> str :
    prefix = strs[0] 
    for i in range(1,len(strs)) :
        while strs[i].find(prefix):
            prefix = prefix[:-1] 
            if prefix == "" : return ""
    return prefix            

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

def search(nums: list[int], target: int) -> int: 
    l = 0
    r = len(nums) - 1
    while l <= r :
        mid = (r + l) // 2 
        if nums[mid] > target :
            r = mid - 1
        elif nums[mid] < target :
            l = mid + 1
        else :
            return mid
    return -1 

# Input: n = 5, bad = 4
# Output: 4

def isBadVersion (version) -> bool : return version >= 4

def firstBadVersion(n: int) -> int: 
    l,r = 1, n 
    while l < r :
        mid = (r + l) // 2 
        if isBadVersion(mid) :
            r = mid
        else :
            l = mid + 1
    return l

                    