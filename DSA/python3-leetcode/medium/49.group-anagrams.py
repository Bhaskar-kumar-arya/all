#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for word in  strs :
            count = [0]*26
            for c in word :
                count[ord(c)-ord('a')] += 1
            groups[tuple(count)].append(word)    
        return list(groups.values())    



                        
# @lc code=end

print(Solution().groupAnagrams(["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"]))