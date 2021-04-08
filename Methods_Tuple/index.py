# tuple.index(element, start, end)
# tuple에서 왼쪽부터 element 처음 등장한 index를 반환한다.
# start, end가 제공되는 경우, 범위를 지정할 수 있다.
# element가 tuple내에 없는 경우에는 'ValueError'가 발생한다.

a = (1,2,3,4,5)
print(a.index(3))
# 2

# print(a.index(6))
# ValueError: tuple.index(x): x not in tuple