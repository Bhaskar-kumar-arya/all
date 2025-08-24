
nums = [3,1,1,3,2,1]
counter = 0
def recurse (nums : list) :
    global counter
    print(nums)
    if len(nums) == 0 : return
    if len(nums) == 1 : 
        counter += nums[0]
        return
    largest = max(nums[1:]) 
    index = len(nums) - nums[::-1].index(largest) - 1
    counter += nums[index-1]
    nums[index] -= index 
    recurse(nums[:index-1])
    recurse(nums[index:])

recurse(nums)
print(counter)    
