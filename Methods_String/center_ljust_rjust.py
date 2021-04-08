# string.center(width[, fillchar])
# 문자열을 가운데로, 양 끝을 fillchar로 채우고 width 만큼의 길이인 문자열로 반환한다.
# 만약 문자열의 길이가 width보다 크다면, 문자열 그대로를 반환한다.
# fillchar이 제공되지 않는 경우, 공백으로 채우고 반환한다.

a = "HELLO"
print(a.center(20))
#        HELLO

print(a.center(20, "*"))
# *******HELLO********

# string.ljust(width[, fillchar])
# 문자열을 왼쪽으로, 나머지를 fillchar로 채우고 width 만큼의 길이인 문자열로 반환한다.
# 만약 문자열의 길이가 width보다 크다면, 문자열 그대로를 반환한다.
# fillchar이 제공되지 않는 경우, 공백으로 채우고 반환한다.

a = "hello"
print(a.ljust(10))
# hello

a = "hello"
print(a.ljust(10, "*"))
# hello*****

# string.rjust(width[, fillchar])
# 문자열을 오른쪽으로, 나머지를 fillchar로 채우고 width 만큼의 길이인 문자열로 반환한다.
# 만약 문자열의 길이가 width보다 크다면, 문자열 그대로를 반환한다.
# fillchar이 제공되지 않는 경우, 공백으로 채우고 반환한다.

a = "hello"
print(a.rjust(10))
#      hello

a = "hello"
print(a.rjust(10, "*"))
# *****hello