
class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue('1')
q.enqueue('2')
q.enqueue('3')
q.enqueue('4')
q.enqueue('5')
print (q.size())
print (q.dequeue())
print (q.dequeue())
print (q.size())

