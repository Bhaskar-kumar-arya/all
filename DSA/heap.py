class MinHeap :

    def __init__(self):
        self.heap = []

    def insert(self,key,value) :
        self.heap.append((key,value))
        self._sift_up(len(self.heap) - 1)

    def peek_min (self) :
        return self.heap[0]
    
    def extractMin (self) :
        minElement = self.heap[0]
        lastElement = self.heap.pop()
        if self.heap :
            self.heap[0] = lastElement
            self._sift_down(0)
        return minElement
    
    def _parent (self,index) :
        return (index - 1) // 2 if index != 0 else None

    def _left(self,index) :
        left = (2*index + 1) 
        return left if left < len(self.heap) else None
    
    def _right(self,index) :
        right = (2*index + 2) 
        return right if right < len(self.heap) else None

    def _sift_down (self,index) :
        while True :
            smallest = index
            left = self._left(index)
            right = self._right(index)
            if left is not None and self.heap[left][0] < self.heap[smallest][0] : smallest = left
            if right is not None and self.heap[right][0] < self.heap[smallest][0] : smallest = right
            if smallest == index : break
            self.heap[smallest],self.heap[index] = self.heap[index],self.heap[smallest]
            index = smallest                              

    def _sift_up (self,index) :
        parentIndex = self._parent(index)
        while parentIndex and self.heap[index][0] <  self.heap[parentIndex][0] : 
            self.heap[index][0],self.heap[parentIndex][0] = self.heap[parentIndex][0] , self.heap[index]
            index = parentIndex 
            parentIndex = self._parent(index)  

    def heapify (self,elements) :
        self.heap = list(elements)
        for i in range(self._parent(len(self.heap) - 1),-1,-1) :
            self._sift_down(i)              