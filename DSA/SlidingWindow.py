from collections import defaultdict
def LongestSubstringWithoutReps (s : str) :
    words = set()
    l = 0
    length = 0
    for r in range(len(s)) :
        if s[r] not in words :
            words.add(s[r])
        else :
            while s[r] in words :
                words.remove(s[l])
                l += 1    
            words.add(s[r]) 
        length = max(length,r - l + 1)        
    return length    

def MaxAVG_SubArray (nums : list[int],k : int) :
    currentSum = sum(nums[0:k])
    maxSum = sum(nums[0:k])
    for r in range(k ,len(nums)) :
        currentSum += nums[r] - nums[r - k] 
        maxSum = max(maxSum,currentSum)
    return maxSum/k    

# iterate through nums with a fixed window size, and evaluate sum
# if target reached , increase window size 
# once you fail to reach target for a window size , retun window size
def minSubArrayLen(target: int, nums: list[int]) -> int:
    length = 999999
    Sum = 0
    l = 0
    for r in range(0,len(nums)) :
        Sum += nums[r]
        if Sum >= target :
            while Sum >= target :
                Sum -= nums[l]
                l += 1 
            length = min(length,r - l + 2)   
    return 0 if length == 999999 else length        



    
print(minSubArrayLen(9,[2,3,1,2,4,3]))

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
