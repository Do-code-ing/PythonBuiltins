# 할당 연산자 (Assignment Operator)
# 변수에 값을 할당한다. 할당하기 전에 요소별로 값을 조작할 수 있다.
# = 을 제외한 할당 연산자는 모두 산수 연산자와 = 가 같이 사용된다.
# =, +=, -=, /=, *=, %=, **=, //= 이 있다.

# 할당 : Assign(=)
a = 7
print(a)
# 7

# 덧셈 후 할당 : Add and Assign(+=)
a += 2
print(a)
# 9

# 뺄셈 후 할당 : Subtract and Assign(-=)
a -= 2
print(a)
# 7

# 나눗셈 후 할당 : Divide and Assign(/=)
a /= 7
print(a)
# 1.0

# 곱셈 후 할당 : Multiply and Assign(*=)
a *= 8
print(a)
# 8.0

# 나눗셈 후 나머지를 할당 : Modulus and Assign(%=)
a %= 3
print(a)
# 2.0

# 거듭제곱셈 후 할당 : Exponent and Assign(**=)
a **= 5
print(a)
# 32.0

# 나눗셈 후 몫을 할당 : Floor-Divide and Assign(//=)
a //= 3
print(a)
# 10.0