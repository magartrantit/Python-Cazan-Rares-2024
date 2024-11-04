class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items == []:
            return None
        return self.items.pop()
    
    def peek(self):
        if self.items == []:
            return None
        return self.items[-1]
    


#Test
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())
print(s.pop())
print(s.pop())