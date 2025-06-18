class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target > nums[-1] or target < nums[0] : return -1
        l,r = 0,len(nums) - 1
        m = (r + l) // 2 
        while l <= r :
            if nums[m] > target :
                r = m - 1 
                m = (r + l) // 2
            elif nums[m] < target :
                l = m + 1
                m =  (r + l) // 2 
            else :
                return m
            
        return -1           

    def isBadVersion(self,version: int) -> bool: return version >= 5
    def firstBadVersion(self, n: int) -> int: 
        l = 1
        r = n 
        while l < r :
            m = (r + l) // 2       
            if self.isBadVersion(m) : 
                r = m
            else :
                l = m + 1       
        return l     

    def searchInsert(self, nums: list[int], target: int) -> int: 
        l = 0 
        r = len(nums) - 1 
        while l <= r :
            m = (l + r) // 2
            if nums[m] > target :
                r = m - 1
            elif nums[m] < target :
                l = m + 1
            else :
                return m
        return l

    def searchRange(self, nums: list[int], target: int) -> list[int]: 
        if not nums : return [-1,-1]        
        # find first occurence 
        l = 0 
        r = len(nums) - 1
        while l < r :
            m = (l + r) // 2
            if nums[m] > target :
                r = m - 1
            elif nums[m] < target:
                l = m + 1 
            else :   
                r = m
        first = l
        if nums[first] != target : return [-1,-1]
        # find last occurence 
        l = first 
        r = len(nums) - 1
        while l < r :
            m  =  (r + l + 1) // 2 
            if nums[m] > target :
                r = m - 1
            elif nums[m] < target:
                l = m + 1 
            else :  
                l = m 
        return [first,r]        
        
    def peakIndexInMountainArray(self, arr: list[int]) -> int: 
        l = 0 
        r = len(arr) - 1 
        while l < r :
            m = (l + r) // 2
            if arr[m + 1] > arr[m] :
                l = m + 1
            else :
                r = m      
        return l
    