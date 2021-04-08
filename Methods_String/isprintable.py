# string.isprintable()
# 문자열의 모든 문자가 인쇄 가능하거나 문자열이 비어있는 경우 True, 아니라면 False를 반환한다.
# 화면에서 인쇄 공간을 차지하는 문자를 인쇄 가능한 문자라고 한다.
# 예를 들어, 문자 및 기호, 숫자, 점, 공백이 있다.

a = "한글"
print(a.isprintable())
# True

a = "\t줄바꿈"
print(a.isprintable())
# False

a = "2+2=4"
print(a.isprintable())
# True

a = chr(29) + chr(97)
print(a.isprintable())
# False
# chr(29)는 탈출 문자라서 안됨

a = chr(97) + chr(97)
print(a.isprintable())
# True