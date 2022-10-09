# 이진탐색 구현

def binary_search(L, x):
    lower = 0               # 리스트의 첫번째 인덱스
    upper = len(L)          # 리스트의 두번째 인덱스

    # 리스트를 반으로 쪼개며 search
    while lower < upper:    # 반복문 종료조건
        middle = (lower + upper) // 2
        if x == L[middle]:
            return middle
        elif x < L[middle]:
            upper = middle - 1
        elif x > L[middle]:
            lower = middle + 1

    return -1               # x가 리스트에 없는 경우 1 리턴

L = [2, 3, 5, 6, 9, 11, 15]
L.sort()

print(binary_search(L, 4))
