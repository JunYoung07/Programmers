from doublylinkedlist import Node
from doublylinkedlist import DoublyLinkedList
# from pythonds.basic.stack import Stack

class LinkedListStack:
    def __init__(self):         # 비어있는 양방향 연결리스트 생성
        self.data = DoublyLinkedList()

    def size(self):             # 양방향 연결리스트의 데이터 개수
        return self.data.getLength()

    def isEmpty(self):
        return self.size == 0

    def push(self, item):
        node = Node(item)
        # 배열의 마지막에 데이터 추가
        self.data.insertAt(self.size() + 1, node)

    def pop(self):
        return self.data.popAt(self.size())

    def peek(self):
        return self.data.getAt(self.size()).data