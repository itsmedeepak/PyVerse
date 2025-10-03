def genFun(x, y):
    return x + y 
    
def latest(v):
    return v + 1

def newFun(m, n, y):
    return latest(genFun(m,n)* y) 

print(newFun(2,2, 4))

#  linkedListCycle
