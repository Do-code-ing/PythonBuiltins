# string.isdecimal()
# 문자열의 문자가 모두 10진수로 이루어졌다면 True, 아니라면 False를 반환한다.
# Numeric_Type = Decimal

a = "12303508"
print(a.isdecimal())
# True

a = "123한글"
print(a.isdecimal())
# False

s = '23455'
print(s.isdecimal())
# True

#s = '²3455'
s = '\u00B23455'
print(s.isdecimal())
# False

# s = '½'
s = '\u00BD'
print(s.isdecimal())
# False

# string.isdigit()
# 문자열의 문자가 모두 분수를 제외한 숫자라면 True, 아니라면 False를 반환한다.
# Numeric_Type = Decimal
# Numeric_Type = Digit

s = '23455'
print(s.isdigit())
# True

#s = '²3455'
s = '\u00B23455'
print(s.isdigit())
# True

# s = '½'
s = '\u00BD'
print(s.isdigit())
# True

# string.isnumeric()
# 문자열의 문자가 모두 분수를 포함한 숫자라면 True, 아니라면 False를 반환한다.
# Numeric_Type = Decimal
# Numeric_Type = Digit
# Numeric_Type = Numeric

s = '1242323'
print(s.isnumeric())
# True

#s = '²3455'
s = '\u00B23455'
print(s.isnumeric())
# True

# s = '½'
s = '\u00BD'
print(s.isnumeric())
# True

s = '1242323'
s='python12'
print(s.isnumeric())
# False