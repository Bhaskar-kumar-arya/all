arr = [3,2,5,9,8]
def insertionSort (array = [] ) : 
    for i in range(len(array)) :
        for j in range(i,0,-1) :
            if array[j] < array[j-1] :
                array[j],array[j-1] = array[j-1],array[j]
            else :
                break


insertionSort(arr)
print(arr)                       
