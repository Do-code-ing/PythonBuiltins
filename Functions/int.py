# int([x])
# int(x, base=10) (base=10 : x는 10진수의 숫자라는 뜻)
# class이며, 숫자나 문자열 x로부터 만들어진 정수 object를 반환한다.
# 실수의 경우, 소수점이 있는 경우, 소수점 아래의 값을 버리고 반환한다.
# arguments가 없다면 0을 반환한다.

# 정수의 경우
print(int(10))
# 10

# 실수의 경우
print(int(12.1))
print(int(12.9))
# 12

# argument가 없는 경우
print(int())
# 0

# x가 숫자가 아니거나 base가 주어진다면,
# x는 문자열이나 bytes 또는 bytearray instance여야 하고, base에 'integer literal'을 알려줘야한다.
# base에 허용되는 값의 범위는 0, 2~36이다. 

# integer literal에 대해 궁금하다면 아래의 주소에 들어가 보도록 하자.
# https://docs.python.org/ko/3/reference/lexical_analysis.html#integers

# 0진수인 문자열을 10진수로 표기
print(int("20", 0))
# 20

# 5진수인 문자열을 10진수로 표기
print(int("20", 5))
# 10

# 8진수인 문자열을 10진수로 표기
print(int("20", 8))
# 16

# 16진수인 문자열을 10진수로 표기
print(int("20", 16))
# 32

# 문자열 앞에 0이 붙는 경우
print(int("020"))
# 20

# 문자열 앞에 0이 붙는 경우에서 8진수로 표기
print(int("020", 8))
# 16

# 0진수인 문자열 중 0이 맨 앞의 숫자인 경우
# print(int("020", 0))
# ValueError: invalid literal for int() with base 0: '020'
# 0진수에서는 0이 맨 앞에 올 수 없음

# 허수와 복소수의 경우
# print(int(10j))
# print(int(123+10j))
# TypeError: can't convert complex to int
# 정수부분을 찾지 못해 TyepError 발생
