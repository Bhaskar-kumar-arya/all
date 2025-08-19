for _ in range(int(input())) :
    input()
    nums = [int(num) for num in input().split()]
    smallest = nums[0]
    possible = True
    for i in range(1,len(nums)) :
        if nums[i] <= nums[i-1] :
            smallest = min(nums[i],smallest)
            continue
        if (smallest)*2 <= nums[i] :
            possible = False
            break
    if possible :
        print('Yes')
    else :
        print('No')
