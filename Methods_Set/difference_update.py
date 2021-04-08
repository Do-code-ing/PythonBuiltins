# set_a.difference_update(set_b)
# 집합 a와 집합 b의 차집합을 집합 a에 갱신한다.

a = {1,2,3,4}
b = {3,4,5,6}
a.difference_update(b)
print(a)
# {1, 2}

# 다음과 같이 표현할 수도 있다.
a = {1,2,3,4}
b = {3,4,5,6}
a -= b
print(a)