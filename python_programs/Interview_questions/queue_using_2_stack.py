class Queue2Stacks(object):
    def __init__(self):
        # Two Stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)


    def dequeue(self):
        # if not self.stack2:
        while self.stack1 != []:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)

print(q.stack1)

for i in range(5):
    print(q.dequeue())

