
for _ in range(int(input())) :
    _,target = list(map(int,input().split()))
    nums = list(map(int,input().split()))

    counter = [0,0,0]
    for num in nums : 
        counter[num] += 1

    _sum = counter[1] + 2*counter[2]

    if _sum > target : 
        print(*nums)
        continue

    if _sum == target :
        print("-1")
        continue

    rem = (target - _sum)

    if rem > 1 : 
        print("-1")
        continue 
    print("0 "*counter[0] + "2 "*counter[2] + "1 "*counter[1])
