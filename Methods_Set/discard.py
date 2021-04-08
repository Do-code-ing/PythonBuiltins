# set.discard(x)
# 집합의 element중 x를 삭제한다.
# x가 없는 경우, 변경사항은 없다.

a = {1,2,3,4}
a.discard(1)
print(a)
# {2, 3, 4}

a = {1,2,3,4}
a.discard(5)
print(a)
# {1, 2, 3, 4}