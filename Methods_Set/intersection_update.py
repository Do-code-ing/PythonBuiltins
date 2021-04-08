# set_a.intersection_update(*other_sets)
# 집합 a와 다른 집합들의 교집합을 집합 a에 갱신한다.

a = {1,2,3,4}
b = {3,4,5,6}
c = {3,5,7}
a.intersection_update(b, c)
print(a)
# {3}

# 다음과 같이 표현할 수도 있다.
a = {1,2,3,4}
b = {3,4,5,6}
c = {3,5,7}
a &= b
a &= c
print(a)