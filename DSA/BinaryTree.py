class Node :
    def __init__(self,val,left : "Node" = None, right : "Node" = None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)    

Root = Node(1,Node(2,Node(4),Node(5)),Node(3,Node(6)))

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

DFS_Stack(Root)