# round(number[, ndigits])
# number를 소수점 다음에 ndigits 정밀도로 반올림한 값을 반환한다.
# ndigits가 생략되거나 None이면, 입력에 가장 가까운 정수를 반환한다.
# 예를 들어, round(5.678, 1) = 5.7 로 5.678의 소수점 1번 째 자리까지 반올림하는 것을 의미한다.

# 정수
int_a = round(10)
print(int_a)
# 10

# float
float_a = round(10.7)
print(float_a)
# 11

# float, ndigits
float_b = round(2.665, 2)
print(float_b)
# 2.67
float_c = round(2.675, 2)
print(float_c)
# 2.67
# 5의 경우, 앞의 숫자가 홀수이면 내리고, 짝수이면 올린다.
# 이는 floating-point number의 경우, 대부분의 소수를 실수로 정확하게 표현할 수 없다는 사실 때문이다.

# 위와 달리 ndigits이 생략될 때
float_d = round(7.5)
print(float_b)
# 8
float_e = round(8.5)
print(float_b)
# 8
# 앞의 숫자인 정수가 홀수이면 올리고, 짝수이면 내린다.

# 정수, ndigits
int_b = round(1235,-1)
print(int_b)
# 1240
int_c = round(1245,-1)
print(int_c)
# 1240
# 이 경우도 마찬가지로, 앞의 숫자가 홀수이면 올리고, 짝수이면 내린다.

# 이 문제에 대해 궁금하다면, 아래의 주소에 들어가 보도록 하자.
# https://docs.python.org/ko/3/tutorial/floatingpoint.html#tut-fp-issues