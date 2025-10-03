# tree creation

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.value) + ",  @" + str(self.left) + ", &" + str(self.right)
    
class breathFirstSearch:
    def __init__(self, root):
        self.stack = [root]
    
    def BFT(self):
        result = []
        while len(self.stack) > 0:
            current = self.stack.pop()
            result.append(current.value)
            
            if current.right is not None:
                self.stack.append(current.right)
            if current.left is not None:
                self.stack.append(current.left)
        return result


root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.right = Node('f')

"""
       a
      / \
     b   c
    / \   \
   d   e   f
     
"""

obj = breathFirstSearch(root)
print(obj.BFT()) 
