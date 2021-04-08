# set_a.intersection(*other_sets)
# 집합 a와 다른 집합들의 교집합을 반환한다.

a = {1,2,3,4}
b = {3,4,5,6}
c = {3,5,7}
print(a.intersection(b, c))
# {3}

# 다음과 같이 표현할 수도 있다.
a = {1,2,3,4}
b = {3,4,5,6}
c = {3,5,7}
print(a & b & c)
# {3}