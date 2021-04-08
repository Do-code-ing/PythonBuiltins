# set_a.union(*other_sets)
# 집합 a와 다른 집합들의 합집합을 반환한다.

a = {1,2,3,4}
b = {3,4,5,6}
c = {5,6,7,8}
print(a.union(b, c))
# {1, 2, 3, 4, 5, 6, 7, 8}

# 다음과 같이 표현할 수도 있다.
a = {1,2,3,4}
b = {3,4,5,6}
c = {5,6,7,8}
print(a | b | c)
# {1, 2, 3, 4, 5, 6, 7, 8}