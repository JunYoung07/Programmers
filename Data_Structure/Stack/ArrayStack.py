class ArrayStack:
    def __init__(self):
        self.data = []      # 빈 스택 초기화

    def size(self):         # 스택의 크기 리턴
        return len(self.data)

    def isEmpty(self):      # 스택이 비어 있는 지 판단
        return self.size() == 0

    def push(self, item):   # 데이터 원소 추가
        self.data.append(item)

    def pop(self):          # 데이터 원소를 삭제 (리턴)
        return self.data.pop()

    def peek(self):         # 스택의 꼭대기 원소 반환
        return self.data[-1]