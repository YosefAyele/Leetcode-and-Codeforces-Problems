class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [0]*self.size
        self.head = 0
        self.tail = 0
        self.curr = 0
        
        self.curr = 0
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.queue[self.head] = value
        self.head = (self.head + 1) % self.size
        self.curr += 1
        
        
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        
        self.tail = (self.tail + 1)%self.size
        
        self.curr -= 1
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.tail]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[(self.head-1)%self.size]
        return -1
    def isEmpty(self) -> bool:
        return self.curr == 0
    def isFull(self) -> bool:
        return self.curr == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()