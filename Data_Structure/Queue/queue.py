from doublylinkedlist import Node
from doublylinkedlist import DoublyLinkedList

class ArrayQueue:
    def __init__(self):         # 빈 큐 초기화
        self.data = []
    def size(self):             # 큐의 크기 리턴
        return len(self.data)
    def isEmpty(self):          # 큐가 비어 있는 지 판단
        return self.size() == 0
    def enqueue(self, item):    # 데이터 원소 추가
        self.data.append(item)
    def dequeue(self):          # 데이터 원소 삭제 (리턴)
        return self.data.pop(0)
    def peek(self):             # 큐의 맨 앞 원소 반환
        return self.data[0]

class LinkedListQueue:
    def __init__(self):
        self.data = DoublyLinkedList()
    def size(self):
        return self.data.getLength()
    def isEmpty(self):
        return self.size() == 0
    def enqueue(self, item):
        node = Node(item)
        self.data.insertAt(self.size() + 1, node)
    def dequeue(self):
        return self.data.popAt(1)
    def peek(self):
        return self.data.getAt(1).data
