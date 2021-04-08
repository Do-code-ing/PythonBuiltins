# dict.setdefault(key[, default_value])
# dictionary에 key가 있는 경우에는 value를 반환하고,
# 그렇지 않은 경우에는 default_value를 반환하고, default_value와 함께 key를 dictionary에 삽입한다.
# default_value가 제공되지 않으면 None이 반환되고 dictionary에 삽입된다.

a = {1:"a", 2:"b", 3:"c"}
print(a.setdefault(1))
# a
print(a.setdefault(4))
# None
print(a.setdefault(5, "e"))
# e
print(a)