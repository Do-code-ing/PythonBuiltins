# 논리 연산자 (Logical Operator)
# 둘 이상의 조건을 결합하는 데 사용할 수 잇는 접속사다.
# and, or, not 이 있다. 

# and (두 조건 모두 만족하는 가)
a = 7>7 and 2>-1
print(a)
# False

# or (두 조건 중 하나라도 만족하는 가)
a = 7>7 and 2>-1
print(a)
# True

# not (논리 연산한 값을 반대로)
a = not(0) # 0 = False
print(a)
# True
a = not(1) # 1 = True
print(a)
# False