# list.remove(element)
# list에서 왼쪽부터 처음 발견된 해당 element를 삭제한다.
# list에 element가 없는 경우, 'ValueError'가 발생한다.

lst = [1,2,4,2,5]
lst.remove(2)
print(lst)
# [1, 4, 2, 5]

# lst.remove(3)
# ValueError: list.remove(x): x not in list