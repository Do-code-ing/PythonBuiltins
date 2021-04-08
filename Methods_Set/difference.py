# set_a.difference(set_b)
# 집합 a와 집합 b의 차집합을 반환한다.

a = {1,2,3,4}
b = {3,4,5,6}
print(a.difference(b))
# {1, 2}

# 다음과 같이 표현할 수도 있다.
a = {1,2,3,4}
b = {3,4,5,6}
print(a - b)
# {1, 2}