# del
# object에 대한 참조를 삭제하는 데 사용된다.
# Python에서는 모든 것이 object이므로, del을 사용하여 variable 참조를 삭제할 수 있다.

a = b = 5
print(a)
# 5
del a
# print(a)
# NameError: name 'a' is not defined

a = ["x", "y", "z"]
del a[1]
print(a)
# ['x', 'y']