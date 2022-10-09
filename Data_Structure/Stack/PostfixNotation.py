'''
# 연산자의 우선순위 설정
prec = {
    '*':3,'/':3,
    '+':2,'-':2,
    '(':1
}

# 중위 표현식을 왼쪽부터 한 글자씩 읽어서 피연사의 경우 출력
# '('이면 push ')'이면 '('가 나올 때까지 pop
# 연산자이면 스택에서 이보다 높(거나 같)은 우선순위 것들을 pop, 출력
# 연산자는 스택에 push
# 스택에 남아 있는 모든 연산자는 모두 pop, 출력

# 스택의 맨 위에 있는 연산자와의 우선순위 비교 // 스택의 peek()연산 이용
# 스택에 남아 있는 연산자 모두 pop()하는 순환문 // while not opStack.isEmpty():

후위표현식 구현하기
'''

class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size == 0

    def push(self, item):
        return self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*':3, '/':3,
    '+':2, '-':2,
    '(':1
}

def postfix(S):
    opStack = ArrayStack()
    answer = ''
    for i in S:
        if i in prec:
            if opStack.isEmpty():
                opStack.push(i)
            else:
                if i == '(':
                    opStack.push(i)
                elif prec[opStack.peek()] < prec[i]:
                    opStack.push(i)
                else:
                    while not opStack.isEmpty() and prec[opStack.peek()] >= prec[i]:
                        answer += opStack.pop()
                    opStack.push(i)
        else:
            if i == ')':
                while opStack.peek() != '(':
                    answer += opStack.pop()
                opStack.pop()
            else:
                answer += i
    while not opStack.isEmpty():
        answer += opStack.pop()
    return answer




