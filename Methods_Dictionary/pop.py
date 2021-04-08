# dict.pop(key[, default])
# dictionary에서 key의 value를 반환하고, 해당 dictionary에서 삭제한다.
# key가 없는 경우 'KeyError'가 발생하는데, default가 주어지면 default를 반환한다.

a = {1:"a", 2:"b"}
print(a.pop(1))
# a
print(a)
# {2: 'b'}

a = {1:"a", 2:"b"}
print(a.pop(3, None))
# None
# key 3이 없으므로 None을 반환
print(a)
# {1: 'a', 2: 'b'}