# 선형탐색 구현

def linear_search(L, x):
    cnt = 1

    if x not in L:
        return -1

    for i in L:
        if i != x:
            cnt += 1
        elif i == x:
            return cnt

L = [2, 5, 4, 9, 7, 1, 6]
print(linear_search(L, 1))

'''
def linear_search(L,x):
    i = 0
    while i < len(L) and L[i] != x:
        i += 1
    if i < len(L):
        return i
    else:
        return -1
'''