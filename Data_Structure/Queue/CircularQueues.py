class CircularQueue:
    def __init__(self, n):          # 빈 큐를 초기화
        self.maxCount = n           # 인자로 주어진 최대 큐 길이 설정
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, item):
        if self.isFull():
            raise IndexError('Queue Full')
        self.rear = (self.rear + 1) % self.maxCount
        self.data[self.rear] = item
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        self.front = (self.front + 1) % self.maxCount
        item = self.data[self.front]
        self.count -= 1
        return item

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front + 1) % self.maxCount]