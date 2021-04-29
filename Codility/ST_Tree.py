#from extratypes import Tree  # library with types used in the task
class Tree(object):
    def __init__(self, x):
        self.x = x
        self.r = None
        self.l = None

def getHeight(T):    
    if (T == None):
        return 0
    leftHeight = rightHeight = 0
    leftHeight = getHeight(T.l)
    rightHeight = getHeight(T.r)
    return max(leftHeight+1, rightHeight+1)

def solution(T):  
    result = getHeight(T)-1
    return result

root = Tree(5)
root.l = Tree(3)
root.r = Tree(10)
root.l.l = Tree(20)
root.l.r = Tree(21)
root.r.l = Tree(1)
root.l.l.l = Tree(1)

print(solution(root))