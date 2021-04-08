# set.remove(element)
# 집합에서 element를 삭제한다.
# 집합에 element가 없는 경우, 'KeyError'가 발생한다.

a = {1,2,3,4}
a.remove(3)
print(a)
# {1, 2, 4}

# a.remove(5)
# KeyError: 5