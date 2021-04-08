# set_a.isdisjoint(set_b)
# 집합 a가 집합 b와 서로소 집합이 맞다면 True, 아니라면 False를 반환한다.

a = {1,2,3,4}
b = {5,6,7,8}
c = {4,5,6,7}
print(a.isdisjoint(b))
# True
print(a.isdisjoint(c))
# False

# 집합이 아니라 다른 type과도 서로소인지 확인할 수 있다.
a = {1,2,3,4,"f"}
b = "1a2bf"
c = [1,2]
d = {1:"a",2:"b"}
e = {"a":1, "b":2}
print(a.isdisjoint(b))
# False
print(a.isdisjoint(c))
# False
print(a.isdisjoint(d))
# False
print(a.isdisjoint(e))
# True