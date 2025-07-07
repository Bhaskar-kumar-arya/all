arr = [3,2,5,9,8]
# each time we introduce a new num , then keep interchanging within the sorted once to get it to its right position
def insertionSort (array = [] ) : 
    for i in range(len(array)) :
        for j in range(i,0,-1) :
            if array[j] < array[j-1] :
                array[j],array[j-1] = array[j-1],array[j]
            else :
                break

# find min num in the non-sorted array, then exchange it with the first non-sorted element - this now becomes a part of sorted array
def selectionSort (array = []) :
    for i in range(len(array)) :
        min_index = i
        for j in range(i + 1 , len(array)) :
            if array[min_index] > array[j] :
                min_index = j
        array[i],array[min_index] = array[min_index],array[i]

# divide into two and arrange (recursion), then use l and r to intermix them in arranged manner
def mergeSort (array = []) :
    length = len(array)
    if length <= 1 : return array
    res = []
    lArray = mergeSort(array[:(length//2)])  
    rArray = mergeSort(array[(length//2):]) 
    
    l = r = 0 
    while l < length // 2 and r < length - (length // 2) :
        if lArray[l] < rArray[r] :
            res.append(lArray[l]) 
            l += 1
        else :
            res.append(rArray[r])  
            r += 1  
    if l == length // 2 :
        res += rArray[r:]
    else :
        res += lArray[l:]
    return res

# divide into three , mid - choose any , left - all smaller than mid right - greater than mid - recurse for left and right - return left + mid + right 
def quickSort (array = []) :
    length = len(array) 
    if length <= 1 : return array
    left = []
    right = []
    for i in range(length - 1) :
        if array[i] <= array[-1] :
            left.append(array[i]) 
        else :
            right.append(array[i])
    return quickSort(left) + [array[-1]] + quickSort(right)         

print(quickSort(arr))                       
 