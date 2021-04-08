# set.pop()
# 집합에서 임의의 element를 반환하고, 해당 집합에서 삭제한다.
# 만약 집합이 비어있다면, 'TypeError'가 발생한다.

a = {1,2,3,4}
print(a.pop())
# 1
print(a)
# {2, 3, 4}
# 숫자의 경우, 제일 작은 수가 반환되고 삭제되는 것 같다.

a = {"a","b","c","d"}
print(a.pop())
# a
print(a)
# {'c', 'd', 'b'}
# 결과가 랜덤하게 나온다.