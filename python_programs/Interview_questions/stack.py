
class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()
print(s.isEmpty())
s.push('1')
s.push('2')
s.push('3')
print("check the peek "+s.peek())
s.push('4')
s.push('5')
print("pop the item "+s.pop())
print("check the size "+ str(s.size()))






