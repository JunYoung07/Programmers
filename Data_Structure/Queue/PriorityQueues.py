from doublylinkedlist import Node, DoublyLinkedList

class PriorityQueue:            # 양방향 리스트로 빈 큐 초기화
    def __init__(self, x):
        self.queue = DoublyLinkedList()

    def size(self):
        self.queue.getLength()

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        newNode = Node(item)
        curr = self.queue.head
        # 작은 수가 우선순위가 높음
        while curr.next.data != None and item < curr.next.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data