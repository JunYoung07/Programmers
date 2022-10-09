# List Insert Practice

def list_insert(L,x):
    idx = 0             # x의 인덱스 값을 표시
    for i in L:         # L의 원소를 하나씩 비교
        # x의 인덱스값
        if x > i:
            idx += 1
        else:
            break

    L.insert(idx, x)    # x를 올바른 인덱스에 삽입
    return L

L = [20, 37, 88, 21, 71]
L.sort()               # L 오름차순 정렬

print(list_insert(L, 40))
