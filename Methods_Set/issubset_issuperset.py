# set_a.issubset(set_b)
# 집합 a가 집합 b의 부분집합이 맞다면 True, 아니라면 False를 반환한다.

a = {1,2,3,4}
b = {1,2,3,4,5}
c = {2,3,4,5}
print(a.issubset(b))
# True
print(a.issubset(c))
# False
print(c.issubset(b))
# True

# 다음과 같이 표현할 수도 있다.
print(a <= b)
# True
print(a <= c)
# False
print(c <= b)
# True

# 진부분집합의 경우, <= 가 아닌 < 로 표기하면 된다.

# set_a.issubset(set_b)
# 집합 a가 집합 b의 상위집합이 맞다면 True, 아니라면 False를 반환한다.
a = {1,2,3,4}
b = {1,2,3,4,5}
c = {2,3,4,5}
print(a.issuperset(b))
# False
print(a.issuperset(c))
# False
print(b.issuperset(c))
# True

# 다음과 같이 표현할 수도 있다.
print(a >= b)
# False
print(a >= c)
# False
print(b >= c)
# True

# 진상위집합의 경우 >= 가 아닌 > 로 표기하면 된다.