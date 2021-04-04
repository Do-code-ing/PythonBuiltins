# pow(base, exp[, mod]) (pow : power, exp : exponent, mod : modulus)
# base의 exp 거듭제곱을 반환한다.
# mod가 있는 경우, base의 exp 거듭제곱을 mod로 나누고 나머지를 반환한다.
# (pow(base, exp) % mod 보다 빠르게 계산한다. (line 34))
# pow(base, exp) 는 거듭제곱 연산자인 base**exp와 같다.

# 양수와 양수
pow_a = pow(2, 2)
print(pow_a)
# 4

# 양수와 음수
pow_b = pow(2, -2)
print(pow_b)
# 0.25

# 음수와 양수
pow_c = pow(-2, 2)
print(pow_c)
# -4

# 음수와 음수
pow_d = pow(-2, -2)
print(pow_d)
# -0.25

# mod를 사용할 때
pow_e = pow(7, 2, 5)
print(pow_e)
# 4
# 7**2 = 49,
# 49 % 5 = 4

# 속도 차이
import time

start = time.time()
for ns in range(100000):
    a = 5
    b = 500
    c = 2
    pow(a, b) % c
print(f"pow({a}, {b}) % {c} : ", time.time()-start)

start = time.time()
for ns in range(100000):
    a = 5
    b = 500
    c = 2
    pow(a, b, c)
print(f"pow({a}, {b}, {c})  : ", time.time()-start)
# Test_1
# pow(5, 500) % 2 :  0.11702632904052734
# pow(5, 500, 2)  :  0.05901288986206055
# Test_2
# pow(50, 500) % 2 :  0.2690610885620117
# pow(50, 500, 2)  :  0.057013511657714844
# Test_3
# pow(500, 500) % 2 :  0.5341203212738037
# pow(500, 500, 2)  :  0.059014081954956055

# base**exp의 값이 클 수록 속도가 빨라지는 듯 하다.
# base**exp가 낮은 숫자라면, 간혹 전자의 경우가 빠른 것 같다.