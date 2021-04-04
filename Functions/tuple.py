# tuple([iterable])
# class이며, argument의 type을 tuple type으로 변환 후 반환한다.
# 기본형은 (element, element ...) 이다.

# 문자열을 tuple로
str_a = "it's a string"
print(type(str_a))
# <class 'str'>
tuple_a = tuple(str_a)
print(type(tuple_a))
# <class 'tuple'>