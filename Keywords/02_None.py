# None (!=0)
# None type으로 아무 값도 없음을 의미하는데,
# 0이나 빈 리스트 등은 각각 int, list type이므로 None type이 아니다.

print(None == 0)
print(None == [])
print(None == False)
# False

x = None
y = None
print(x == y)
# True

# 함수에서 아무 값도 return 받지 않을 때 None을 return한다.
def none_func():
    a = 1
    b = 2
    c = a + b
print(none_func())
# None