# number

# int.bit_length()
# 부호와 선행 0을 제외하고, 이진수로 정수를 나타내는 데 필요한 비트 수를 반환한다.

n = 37
print(f"{n:b}")
# 100101
print(n.bit_length())
# 6

# int.to_bytes(length, byteorder, *, signed=False)
# 정수를 나타내는 바이트의 배열을 반환한다.

n = 15
print(n.to_bytes(2, byteorder="big"))
print(n.to_bytes(10, byteorder="big"))
print(n.to_bytes(2, byteorder="little"))

# int.as_integer_ratio()
# 분수의 분모와 분자를 정수로 각각 반환한다.

n = 2
m = 2.5
print(n.as_integer_ratio())
# (2, 1)
print(m.as_integer_ratio())
# (5, 2)

# float.is_inetger()
# float instance가 정수값을 가진 유한이면 True, 아니라면 False를 반환한다.

n = 1.0
m = 1.5
print(n.is_integer())
# True
print(m.is_integer())
# False

# float.hex()
# 부동 소수점의 16진수 문자열 표현으로 반환한다.
# 유한 부동 소수점의 경우, 0x가 선행하며 p와 지수가 후행한다.

print(n.hex())
print(m.hex())

# iterater

a = [1,2,3,4,5]
print(a)
iter_a = a.__iter__()
print(iter_a)
print(iter_a.__next__())
print(iter_a.__next__())
print(next(iter_a))
print(list(iter_a))

# sequence

a = "hi"
b = "hello"
a += b # 이어쓰기
print(a)
# hihello
a = " ".join(a) # 문자 사이 사이에 끼어 넣기
print(a)
# h i h e l l o

lst = [[]]*3
print(lst)
lst[0].append(3)
print(lst)
lst[0].append(1)
print(lst)
lst[0].append(2)
print(lst)
# 모든 list에 작동
# 복사본을 복제한 것이 아니라 참조본을 복제한 것
# 아래의 예시는 복사본을 복제한 것

# 다차원 sequence
lst = [[] for i in range(3)]
print(lst)
lst[0].append(3)
lst[0].append(3)
lst[1].append(5)
lst[1].append(6)
lst[2].append(7)
lst[2].append(8)
print(lst)
for i in range(len(lst)):
    lst[i] = sum(lst[i])
print(lst)

lst = [[None]*2 for i in range(3)]
print(lst)
lst[0][0] = 3
print(lst)

lst = [1,2,3,4,5]
for idx, x in enumerate(lst):
    lst[idx] = x+1

print(lst)
del lst[0]
print(lst)
lst.append(7)
print(lst)