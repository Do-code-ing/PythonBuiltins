# list([iterable])
# class이며, argument의 type을 list type으로 변환 후 반환한다.
# 기본형은 [element, element ...] 이다.

# 문자열을 list로
str_a = "it's a string"
print(type(str_a))
# <class 'str'>
lst_a = list(str_a)
print(type(lst_a))
# <class 'list'>