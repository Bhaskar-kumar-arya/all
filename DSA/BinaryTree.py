from collections import deque
class Node :
    def __init__(self,val,left : "Node" = None, right : "Node" = None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)   
    def __repr__(self):
        return str(self.val) 
#         1
#     2       3  
#   4   5   6
# 7
Root = Node(1,Node(2,Node(4,Node(7)),Node(5)),Node(3,Node(6)))
symmetricNode = Node(1,Node(2,Node(3),Node(4)),Node(2,Node(4),Node(3))) 
InOrderTreeRoot = Node(5,Node(4,Node(3),Node(5)),Node(6))

def DFS (root : Node) :
    if not root : 
        return
    print(root)
    DFS(root.left)
    DFS(root.right)

  

def DFS_Stack (root : Node) :
    stack = [root]
    while stack :
        node = stack.pop()
        print(node.val)
        if node.right : stack.append(node.right) 
        if node.left : stack.append(node.left)   

def BinarySearchForNumber (val : int ,root : Node = None) -> Node : 
    if not root : return None
    if root.val > val : return BinarySearchForNumber(val,root.left) 
    if root.val < val : return BinarySearchForNumber(val,root.right)
    return root



def inOrderTraversal_Recursive (root : Node) :
    if not root : return
    inOrderTraversal_Recursive(root.left) 
    print(root)
    inOrderTraversal_Recursive(root.right)

  
def inOrderTraversal_stack (root : Node) :
    result = []
    stack = []
    curr : Node = root
    while stack or curr :
        while curr :
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    print(result)        

def BFS (root : Node) : 
    q = deque()
    q.append(root)
    while q :
        node = q.popleft()
        print(node.val)
        if node.left : q.append(node.left) 
        if node.right : q.append(node.right)

def postorderTraversal_iterative(root: Node) -> list[int]:
    result = []
    stack = [root]    
    while stack : 
        node = stack.pop()
        result.append(node.val)
        if node.left: stack.append(node.left)
        if node.right : stack.append(node.right)
    print(list(reversed(result)))

# go deep down on left
# when curr = none ,  go right once,then continue
# if right was also empty ,
# pop it... set it as prev
def postorderTraversal_iterative_noReverse(root: Node) -> list[int]:
    result = []
    stack = []
    prev = None
    curr = root
    while stack or curr :
        while curr :
            stack.append(curr)
            curr = curr.left
        node = stack[-1]
        if not node.right or prev == node.right :
            result.append(node.val)
            prev = node
            stack.pop()
        else : 
            curr = node.right
    print(result)        

        
def MaxDepth_recursion (root : Node) :
    if not root : return 0
    return 1 + max(MaxDepth_recursion(root.left),MaxDepth_recursion(root.right))

def MaxDepth_stack (root : Node) :
    max_depth = 0
    curr_depth = 0
    prev : Node = None
    curr : Node = root
    stack = []
    while stack or curr :
        while curr : 
            stack.append(curr)
            curr = curr.left
            curr_depth += 1    
        node = stack[-1]
        if not node.right or prev == node.right :
            prev = node
            curr = None
            stack.pop()     
            curr_depth -= 1
        else : 
            curr = node.right
            curr_depth += 1
        max_depth = max(max_depth,curr_depth)
    print(max_depth)

def isSymmetric_helper(left_node,right_node) :
    if left_node == None : 
        if right_node == None : 
            return True 
        else : return False
    if left_node.val != right_node.val :
        return False
    if isSymmetric_helper(left_node.right,right_node.left) and isSymmetric_helper(left_node.left,right_node.right) : 
        return True 
    else : return False

def isSymmetric_recursion(root: Node) -> bool: 
    return isSymmetric_helper(root.left,root.right)

def ToArray_levelOrder (root : Node) :
    result = [] 
    q = deque()
    q.append(root)
    while q :
        node = q.popleft()
        if node : 
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else :
            result.append(None)
        
    return result


def isSymmetric_FromArray (tree : list[Node]) :
    for i in range(len(tree)//4) :
        reduced_tree = tree[2**i - 1:2**(i + 1) - 1]
        if reduced_tree != list(reversed(reduced_tree)) : return False
    return True           
           

