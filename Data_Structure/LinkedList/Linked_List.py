# Linked_List

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList : empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += '->'
            curr = curr.next
        return s

    def getAt(self, pos):
        if pos <= 0 and pos > self.nodeCount: return None
        i = 1
        curr = self.head
        while  i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        curr = self.head
        answer = []
        while curr != None:
            answer.append(curr.data)
            curr = curr.next
        return answer

    def insertAt(self, pos, newNode):
        if pos < 1 and pos > self.nodeCount + 1: return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = getAt(pos - 1)
            newNode.newt = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if not pos >= 1 and pos <= nodeCount:
            return IndexError

        if pos == 1:
            curr = self.head
            if pos == self.nodeCount:
                self.head = None
                self.tail = None
            else:
                self.head = curr.next
        else:
            prev = self.getAt(pos - 1)
            if pos == self.nodeCount:
                curr = self.tail
                prev.next = None
            else:
                curr = prev.next
                prev.next = curr.next

        self.nodeCount -= 1
        return curr.data

    def insertAfter(self, prev, newNode):
        

    def popAfter(self, prev):

