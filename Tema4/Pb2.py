class Queue:

    def __init__(self):
        self.items = []
    
    def pop(self):
        if self.items == []:
            return None
        return self.items.pop(0)
    
    def push(self, item):
        self.items.append(item)

    def peek(self):
        if self.items == []:
            return None
        return self.items[0]
    
#Test
q = Queue()
q.push(1)
q.push(2)
q.push(3)
print(q.peek())
print(q.pop())
print(q.pop())
