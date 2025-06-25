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
           

def isSymmetric_stack (root : Node) :
    lStack = [root.left]
    rStack = [root.right]
    while lStack and rStack : 
        leftNode = lStack.pop()
        rightNode = rStack.pop()
        if leftNode is None and rightNode is None : continue
        if leftNode is None or rightNode is None : return False
        if leftNode.val != rightNode.val : return False
        lStack.append(leftNode.left)
        lStack.append(leftNode.right)
        rStack.append(rightNode.right)
        rStack.append(rightNode.left)
    return True

# combined with max depth calculation .. while calculating the depth , we simultaneously check if it is balanced
def isBalanced_recursion (root : Node) :
    if not root : return (0)
    leftDepth = isBalanced_recursion(root.left)
    rightDepth= isBalanced_recursion(root.right)
    return (1 + max(leftDepth,rightDepth) if abs(leftDepth - rightDepth) <= 1 and leftDepth != -1 and rightDepth != -1 else -1)          

# output for Root Node : [[1], [2, 3], [4, 5, 6], [7]]
def levelOrder_stack (root) : 
    if not root : return []
    result = []
    q = deque()
    q.append(root)
    while q :
        temp = []
        for i in range(len(q)) :
            node = q.popleft()
            temp.append(node.val)
            if node.left : q.append(node.left)
            if node.right : q.append(node.right)    
        result.append(temp)    
    return result        

def invertTree(root : Node) -> Node : 
    if not root : return None
    root.left , root.right = root.right,root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

def printTree (root : Node) :
    levels = levelOrder_stack(root)
    for level in levels :
        print(level) 

def hasPathSum_postOrder(root: Node, targetSum: int) -> bool:
    stack = []
    curr = root
    prev : Node = None
    sum = 0
    while stack or curr :
       
        while curr :
            stack.append(curr)
            sum += curr.val
            curr = curr.left
        node = stack[-1]
        if not node.right or prev == node.right :
            if not node.right and not node.right :
                if sum == targetSum : return True
            stack.pop()
            prev = node
            sum -= node.val 
            curr = None   
        else : 
            curr = node.right
    return False        

def hasPathSum_preOrder(root: Node, targetSum: int) -> bool:   
    stack = [(root,root.val)]
    while stack :
        node,curr_sum = stack.pop()
        if not node.left and not node.right and curr_sum == targetSum : return True
        if node.right : stack.append((node.right,curr_sum + node.right.val))
        if node.left : stack.append((node.left,curr_sum + node.left.val))
    return False

def hasPathSum_Recursion (root : Node,targetSum : int) :
    if not root : return False
    if targetSum == root.val and not root.left and not root.right : return True
    targetSum -= root.val
    if hasPathSum_Recursion(root.left,targetSum) or hasPathSum_Recursion(root.right,targetSum) : return True
    return False

def search (root : Node , node) :
    if not root : return False
    if search(root.left,node) or search(root.right,node) : return True
    if root == node : return True
    return False

def lowestCommonAncestor_DFS(root: Node, p: Node, q: Node) -> Node :
    stack = []
    curr = root
    prev = None
    while stack or curr :
        while curr :
            stack.append((curr,[curr == p,curr == q]))
            # print(f"curr : {curr} , p : {p} , q : {q} , stack[-1][1][0] : {stack[-1][1][0]} , stack[-1][1][1] : {stack[-1][1][1]}")
            curr = curr.left
        node,isAscendant = stack[-1]
        if not node.right or prev == node.right :
            stack.pop()
            if isAscendant == [True,True] : return node
            prev = node
            if isAscendant[0] : stack[-1][1][0] = True
            if isAscendant[1] : stack[-1][1][1] = True    
        else : 
            curr = node.right
    return None    

def lowestCommonAncestor_ParentMap (root: Node, p: Node, q: Node) -> Node :
    parent = {root : None}
    stack = [root]
    while p not in parent or q not in parent : 
        node =stack.pop()
        if node.left : 
            stack.append(node.left)
            parent[node.left] = node
        if node.right : 
            stack.append(node.right)
            parent[node.right] = node
    Ancestors = set()
    while p : 
        Ancestors.add(p)
        p = parent[p]
    while q not in Ancestors :
        q = parent[q]
    return q        

def lowestCommonAncestor_recursion (root: Node, p: Node, q: Node) :
    if not root : return None 
    if root == p or root == q :
        return root
    left = lowestCommonAncestor_recursion(root.left,p,q) 
    right = lowestCommonAncestor_recursion(root.right,p,q) 
    if left and right : return root
    return left if left else right

root = Node(3)

root.left = Node(5)
root.right = Node(1)

root.left.left = Node(6)
root.left.right = Node(2)

root.right.left = Node(0)
root.right.right = Node(8)

root.left.right.left = Node(7)
root.left.right.right = Node(4)

# to do : use hasmap for inorder ...
def buildTree(preorder: list[int], inorder: list[int]) -> Node:
    def recurse () : 
        if not inorder : return 
        root = Node(preorder[0]) 
        root.left = buildTree(preorder[1:],inorder[:inorder.index(root.val)]) 
        root.right = buildTree(preorder[inorder.index(root.val) + 1 :],inorder[inorder.index(root.val) + 1 :])
        return root
    return recurse()

printTree(buildTree([3,9,20,15,7],[9,3,15,20,7]))    

