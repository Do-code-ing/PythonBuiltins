# dict.update([other])
# dictionary에 key와 value를 나타내는 other에서 key가 있으면 value를 갱신하고,
# 없다면 key와 value를 dictionary에 삽입한다.
# 아무것도 제공되지 않은 경우, 아무 것도 변하지 않는다.

a = {1:"a", 2:"b"}
a.update({1:"A"})
print(a)
# {1: 'A', 2: 'b'}
a.update({3:"c"})
print(a)
# {1: 'A', 2: 'b', 3: 'c'}

# 다음과 같은 방법으로 변수를 dictionary에 삽입할 수 있다.
a.update(z = 15) # 숫자는 변수명의 제일 앞 글자가 될 수 없어서 z로 했다.
print(a)
# {1: 'A', 2: 'b', 3: 'c', 'z': 15}

# 아무것도 제공되지 않은 경우
a.update()
print(a)