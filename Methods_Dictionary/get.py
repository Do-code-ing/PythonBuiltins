# dict.get(key[, value])
# 해당 key의 value를 반환한다.
# key가 없다면 None을 반환한다.
# key가 없으며 value가 제공될 경우, 새로 제공한 value를 반환한다.

a = {1:"a", 2:"b", 3:"c"}
print(a.get(1))
# a
print(a.get(4))
# None
print(a.get(2, "B"))
# b
# key 2가 있으므로 B가 아닌 b를 반환
print(a.get(4, "d"))
# d
# key 4가 없으므로 d 반환

# get()은 반환만 해주므로 새 key와 value를 만들지 않음에 주의
# 새 key와 value를 만들어주고 싶다면,
# a[4] = "d" 와 같이 작성할 것