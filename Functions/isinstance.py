# isinstance(object, classinfo)
# object argument가 classinfo argument인지, 또는
#                   classinfo의 (직간접적인 혹은 가상의)subclass의 instance라면 True를 반환한다.
# object가 classinfo에서 주어진 type의 object가 아니라면 항상 False를 반환한다.
# classinfo가 type objects로 이루어진 tuple이면, object가 그 type중에 하나의 instance일 때 True를 반환한다.
# classinfo가 type이나 types로 이루어진 tuple이 아니라면, 'TypeError'가 발생한다.

# instance가 class에 속해 있는지
class Something:
    def __init__(self):
        pass

sth = Something()
print(isinstance(sth, Something))
# True

# 숫자 10이 int class에 속해 있는지
print(isinstance(10, int))
# True

# 숫자 10이 str class에 속해 있는지
print(isinstance(10, str))
# False

# 10이 tuple_a에 속해 있는지
tuple_a = str, int
print(isinstance(10, tuple_a))
# True

# tuple의 내용에 문자열이 있는 경우
tuple_b = "str", int
# print(isinstance(10, tuple_b))
# TypeError: isinstance() arg 2 must be a type or tuple of types