# string.capitalize()
# 문자열의 첫 문자를 대문자로, 나머지 문자들을 소문자로 변환 후 반환한다.
# 첫 문자가 a-z가 아니면 나머지 문자들만 소문자로 변환 후 반환한다.

a = "hello WORLD"
print(a.capitalize())
# Hello world

a = "+hello WORLD"
print(a.capitalize())
# +hello world