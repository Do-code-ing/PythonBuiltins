# format(value[, format_spec]) (format_spec : Format Specification Mini-Language)
# value를 fromat_spec에 맞게 구성하여 반환한다.
# format_spec의 기본값은 빈 문자열이며, 일반적으로 str(value)를 호출하는 것과 같은 효과를 준다.

a = 2+3

# 정수의 경우
a = format(a)
print(a)
# 5

# 10진수의 정수를 8진수로 format
b = 10+10
b = format(b, "o")
print(b)
# 24

# 참고
# format(value, format_spec) 에 대한 호출은
# type(value).__format__(value, format_spec) 로 번역되는데,
# value의 __format__() method를 검색할 때 instance dictionary를 건너뛴다.
# method 검색이 object 에 도달하고 format_spec 이 비어 있지 않거나,
# format_spec 또는 반환 값이 문자열이 아닌 경우 TypeError 예외가 발생한다.

# Format Specification Mini-Language 에 관하여 알고싶다면 아래의 주소에 들어가 보도록 하자.
# https://docs.python.org/ko/3/library/string.html#formatspec