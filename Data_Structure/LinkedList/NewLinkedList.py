class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        # LinkedList 맨 앞에 dummyNode 생성
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next is not None:
                s += '->'
        return s

    def getLength(self):
        return self.nodeCount

    # 리스트 순회
    def traverse(self):
        result = []
        curr = self.head
        # curr.next가 존재하면 반복 (None의 경우 반복문 탈출)
        while curr.next:
            # dummyNode를 추가하지 않는
            curr = curr.next
            result.append(curr.data)
        return result

    # 리스트 탐색
    def getAt(self, pos):
        if pos < 0 and pos > self.nodeCount:
            return None
        # i = 0일 때 dummyNode
        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    # 노드 삽입 1
    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True

    # 노드 삽입 2
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False
        # self.head가 dummyNode이기 때문에 pos == 1의 경우를 생각하지 않아도 됨.
        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    # 노드 제거 1
    def popAfter(self, prev):
        curr = prev.next
        if prev.next is None:
            return None
        if curr.next is None:
            self.tail = prev
        prev.next = curr.next
        self.nodeCount -= 1
        return curr.data

    # 노드 제거 2
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return IndexError
        prev = self.getAt(pos - 1)
        return self.popAfter(prev)

    # 리스트 합치기
    def concat(self, L):
        self.tail.next = L.head.next
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount