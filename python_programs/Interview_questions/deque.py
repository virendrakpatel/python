
class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0,item)

    def addRear(self, item):
        self.item.append(item)

    def removeFront(self):
        return self.item.pop(0)

    def removeRear(self):
        return self.item.pop(-1)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

ls = [1,2,3,4,5,6]
print (ls[-1])
