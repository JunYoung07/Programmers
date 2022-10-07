def Binary(L, x, lower, upper):
    if lower > upper:
        return -1
    middle = (lower + upper) // 2
    if x == L[middle]:
        return middle
    elif x < L[middle]:
        return Binary(L, x, lower, middle - 1)
    else:
        return Binary(L, x, middle + 1, upper)


L = [2, 5, 7, 9, 11]
L.sort()

print(Binary(L, 4, 0, 4))