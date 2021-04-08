# dict.popitem()
# dictionary에 가장 최근에 삽입된 item(key, value)를 반환하고, 해당 dictionary에서 삭제한다.

a = dict()
a[1] = "a"
a[3] = "c"
a[2] = "b"
print(a.popitem())
# (2, 'b')
print(a)
# {1: 'a', 3: 'c'}