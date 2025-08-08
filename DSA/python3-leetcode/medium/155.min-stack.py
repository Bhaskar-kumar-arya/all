#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.arr = []
        self.min = []
    def push(self, val: int) -> None:
        self.arr.append(val)
        self.min.append(min(val,self.min[-1]) if len(self.min) > 0 else val)
        


    def pop(self) -> None:
        self.arr.pop()
        self.min.pop()
 

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

stack = MinStack()
stack.push(6)
stack.push(6)
stack.push(7)
stack.pop()
stack.pop()
stack.pop()
stack.push(7)
stack.push(-8)


print(stack.getMin())