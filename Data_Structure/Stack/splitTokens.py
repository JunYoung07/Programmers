'''
후위 표기식에서 입력받은 수가 몇자리 수인지 모르기 때문에
수식이 문자열로 주어졌을 때 이를 연산자와 피여산자로 나누어 준다.
'''

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