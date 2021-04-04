# divmod(a, b) : division module
# 두 개의 (복소수가 아닌)숫자를 arguments로 취하고,
# 정수 나누기를 사용할 때의 몫과 나머지로 구성된 한 쌍의 숫자를 반환한다.
# 예를 들어, divmod(a, b) 의 결과는 (a // b , a % b) 와 같다.

print(divmod(5,2))
# (2, 1)
print(divmod(5,-2))
# (-3, -1)
print(divmod(-5,-2))
# (2, -1)
print(divmod(-5,2))
# (-3, 1)

print(divmod(2, 0.3))
# (6.0, 0.20000000000000007)

# 참고
# divmod(a, b)
# a == (a // b) * b + a % b
# divmod(2, 0.3)
# 2 == # 6.0 * 0.3 + 0.20000000000000007
# if a % b != 0:
# 0 <= abs(a % b) < abs(b)

