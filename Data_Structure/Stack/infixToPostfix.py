from stacks import ArrayStack as Stack

# 받아들이는 인자가 list로 되어있음
# 후위 표현식도 list에 담는다.

# exprStr -> 중위 표현식의 수식
def splitTokens(exprStr):
    tokens = []
    # 숫자의 자릿수 계산하기 123의 경우 -> 1 * 10^2 + 2 * 10^1 + 3 * 10^0
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True    # 수를 만났으므로 True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)
    return tokens

def infixToPostfix(tokenList):
    prec = {
        '*':3,
        '/':3,
        '+':2,
        '-':2,
        '(':1,
    }

    opStack = Stack()
    postfixList = []

    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)

        elif token == '(':
            opStack.push(token)
        elif token == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        else:
            if opStack.isEmpty():
                opStack.push(token)
            else:
                if prec[opStack.peek()] < prec[token]:
                    opStack.push(token)
                else:
                    while not opStack.isEmpty() and prec[opStack.peek()] >= prec[token]:
                        postfixList.append(opStack.pop())
                    opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return postfixList

def postfixEval(postfixList):
    cStack = Stack()
    # result = 0

    for i in postfixList:
        if type(i) is int:
            cStack.push(i)
        elif i in '*/+-':
            first = cStack.pop()
            second = cStack.pop()
            if i == '+':
                new = second + first
            elif i == '-':
                new = second - first
            elif i == '*':
                new = second * first
            else:
                new = second / first
            cStack.push(new)

    return cStack.pop()


def solution(expr):
    # 중위 표현식을 token의 리스트로 바꾼다. (연산자/피연산자 구분)
    tokens = splitTokens(expr)
    # 중위 표현식을 후위 표현식으로 변환 (리스트 내부에 후위 표현식 순서로 연산자와 피연산자 저장)
    postfix = infixToPostfix(tokens)
    # 후위 표현식으로 된 식을 계산
    val = postfixEval(postfix)
    return val