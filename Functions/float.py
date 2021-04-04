# float([x])
# class이며, 숫자나, 문자열 x를 실수로 만들어 반환한다.
# arguments가 문자열이면, 10진수를 포함해야 하고, 부호가 앞에 오는 경우, 필요하다면 공백으로 둘러 쌓아도 된다.
# 부호 : '+', '-'
# 무한대 : 'infinity','inf'
# nan : Not a Number
# 어떤 arguments도 넣어주지 않으면 0.0 을 반환한다.

# 공백인 경우
print(float())
# 0.0

# 정수인 경우
print(float(-610))
# -610.0
print(float(999 + 20))
# 1019.0
# 999 + 20 은 python 내에서 1019 로, 수식이기에 하나의 숫자로 취급하여 사용 가능

# 문자열인 경우
print(float(" -610 "))
# -610.0
print(float("NaN"))
# nan
print(float("infinity"))
# inf
print(float("-inf"))
# -inf
# print(float("211 - 120"))
# "211 -120" 은 문자열이기 때문에 불가능
# 사용하고 싶다면 eval() 을 통해 평가하여 사용가능
print(float(eval("211-120")))
# 91.0

# 참고
# arguments가 'Python float'의 범위에서 벗어나면, 'OverflowError'가 발생한다.