# building a stack using Linked List in Python

# building the Nodes for linked list
class Node:
    def __init__(self, x):
        self.value = x
        self.next = None

# building a Stack class
class Stack:
    def __init__(self):
        self.top = None   # in arrays, we use -1
        self.size = 0
    
    def is_empty(self):
        return self.top is None

    def push(self, x):
        node = Node(x)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):    # for popping the first element of the stack: FIFO
        if self.is_empty():
            return None
        pop_data = self.top.value
        self.top = self.top.next
        self.size -= 1
        return pop_data
    
    def peek(self):   # for looking at the top of the stack
        if self.is_empty():
            return None
        return self.top.value
    
    def __str__(self):    # display the Stack using string representation
        if self.is_empty():      
            return "Stack is empty"
        current = self.top
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        return  "" + " -> ".join(elements)
    
    def get_size(self):
        return self.size
    
if __name__ == '__main__':
    stack = Stack()
    stack.push(56)
    stack.push(41)
    stack.push(96)

    print(stack)
    print("Peek at stack: ", stack.peek())

    data = stack.pop()
    print(f"Value popped: {data}")
    print(stack)

    stack.push(28)
    print(stack)
