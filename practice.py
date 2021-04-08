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

# append와 extend 차이점
lst1 = [1,2,3]
lst2 = [4,5,6]
lst1.append(lst2)
print(lst1)
#[1, 2, 3, [4, 5, 6]]

lst1 = [1,2,3]
lst2 = [4,5,6]
lst1.extend(lst2)
print(lst1)
# [1, 2, 3, 4, 5, 6]

lst1 = [1,2,3]
lst2 = [4,5,6]
lst1 += lst2
print(lst1)
# [1, 2, 3, 4, 5, 6]

lst = [1,2,3,4]
cha = lst.pop()
print(lst)
print(cha)

lst = ["h","e","l","l","o"]
lst.reverse()
print(lst)

str_a = "hello"
str_b = list(reversed(str_a))
print(str_b)

lst = ["h","e","l","l","o"]
lst[::2] = "H","L","O"
print(lst)

lst = list("abc")
print(lst)

# list
lst = ['c', 'a', 'b']
lst.sort(reverse=True)
print(lst)

# tuple
tuple_a = tuple("abc")
print(tuple_a)

tuple_a = tuple(["abc","bcd","efg"])
print(tuple_a)

# str

# str.capitalize()
# 문자열의 첫 문자를 대문자로, 나머지 문자를 소문자로 반환한다.
str_a = "hello"
str_b = str_a.capitalize()
print(str_b)

# str.casefold()
str_a = "ß" # 독일어
str_b = str_a.casefold()
str_c = str_a.lower()
print(str_b)
print(str_c)

# str.center(width[, fillchar])
str_a = "abba"
str_b = str_a.center(10, "h")
print(str_b)

# str.encode(encoding="utf-8", errors="strict")
# encoding

# str.endswith(suffix[, start[, end]])
# suffix로 끝나는 문자열이 맞다면 True, 아니라면 False 반환
str_a = "hello"
str_b = str_a.endswith("o", 0, 4)
print(str_b)

# str.expandtabs(tabsize=8)
str_a = "hello\tmy\tdear"
print(str_a)
str_b = str_a.expandtabs(tabsize=4)
print(str_b)

# str.find(sub[, start[, end]])
str_a = "hellell"
str_b = str_a.find("ell")
print(str_b)

# str.format(*args, **kwargs)
str_a = "{}, please {}.".format("Hey", "shut up")
print(str_a)
str_b = "Hello {}, your balance is {:9.3f}".format("Adam", 230.2346)
print(str_b)

# str.format_map(mapping)
point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))

point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format_map(point))

class Coordinate(dict):
    def __missing__(self, key):
      return key


print('({x}, {y})'.format_map(Coordinate(x='6')))
print('({x}, {y})'.format_map(Coordinate(y='5')))
print('({x}, {y})'.format_map(Coordinate(x='6', y='5')))

# str.isalnum() # alphabet, number
str_a = "w1"
print(str_a.isalnum())

# str.isalpha()
str_a = "w221"
print(str_a.isalpha())

# str.isascii()
# str.isdecimal() # 십진수 문자열만
str_a = "010"
print(str_a.isdecimal())
# str.isdigit() # 다른 유니코드 지원 문자에 대해
print(str_a.isdigit())

# str.islower()
# 모두 소문자인지

# str.isnumeric()
str_a = "Ⅲ" # 분수, 로마숫자, 통화숫자, 등등 도 가능
print(str_a.isnumeric())

# str.isprintable()
# print 할 수 있는지
# \n 이런거 있으면 False

# str.isspace()
# 한 개 이상의 공백 문자로 이루어져 있는지

# str.istitle()
str_a = "Hello" # 첫 문자만 대문자인 경우 = title case string
str_b = "hello"
str_c = "HEllo"
print(str_a.istitle())
print(str_b.istitle())
print(str_c.istitle())

# str.isupper()
# 모두 대문자인지

# str.join(iterable)
str_a = "ABC"
iter_a = ["a","b"]
str_b = str_a.join(iter_a)
print(str_b)

# str.ljust(width[, fillchar])
# 문자열을 왼쪽 정렬하고 길이가 width만큼인 문자열로 반환, fillchar이 있는 경우 빈 부분을 fillchar로 채운다.
str_a = "ABC"
str_b = str_a.ljust(10, "0")
print(str_b)

# str.lower()
# 모두 소문자로 돌려줌

# str.lstrip([chars])
# 왼쪽부터 chars에 해당하는 것들 다 지우고, 해당하는게 없으면 stop, 반환
str_a = "www.naver.com"
print(str_a.lstrip('.wa'))
print(str_a.removeprefix("www.")) # 왼쪽에서 부터 해당하는 것만 지우기

# str.maketrans(x[, y[, z]])
# str.translate()에 사용할 수 있는 translate table을 반환한다.
# x만 있는 경우, 유니코드 포인트(정수) 또는 문자(길이가 1인 문자열)을
# 유니코드 포인트, 문자열(임의의 길이) 또는 None으로 매핑하는 dictionary여야 한다.
# 문자 키는 유니코드 포인트로 변환된다.

txt = "hello"
dic_a = {"h":"y"}
mytable = "".maketrans(dic_a)
print(txt.translate(mytable))






# str.partition(sep)
# sep을 기준으로 (sep 앞의 문자열), (sep), (sep 뒤의 문자열)인 tuple로 반환
str_a = "www.naver.com"
print(str_a.partition("."))

# str.removeprefix(prefix)
# prefix로 시작하면 prefix 이 후의 문자열 반환
# 아니라면 그대로 반환
str_a = "www.naver.com"
print(str_a.removeprefix("www."))

# str.removesuffix(suffix)
# suffix로 끝나면 suffix 전의 문자열 반환
str_a = "www.naver.com"
print(str_a.removesuffix(".com"))

# str.replace(old, new[, count])
# 모든 old 문자를 new 문자로 바꾸고, count가 있으면 count개의 문자만 바꾸고 반환
str_a = "www.naver.com"
print(str_a.replace("www", "http://www"))
str_b = "abcaaabc"
print(str_b.replace("a", "A", 3))

# str.rfind(sub[, start[, end]])
# sub 중 가장 큰 index 반환
str_a = "abcabcabc"
print(str_a.rfind("a"))
print(str_a.rfind("a", 0, 5))

# str.rindex(sub[, start[, end]])
# rfind()와 비슷하지만, 찾을 수 없는 경우 ValueError 발생

# str.rjust(width[, fillchar])
# ljust()과 같으며 반대 방향으로

# str.rpartiton(sep)
# partition()에서 sep을 찾을 때 반대 순서로 찾아서 반환

# str.rsplit(sep=None, maxsplit=-1)
# split()과 같으며 반대 방향으로

# str.rstrip([chars])
# strip()과 같으며 반대 방향으로

# str.split(sep=None, maxsplit=-1)
# sep을 기준으로 문자열을 나누어 list로 반환
# sep이 주어지지 않는다면 공백 문자를 기준으로 반환 
# maxsplit이 주어지면 그 숫자만큼만 반복
str_a = "www.naver.com"
print(str_a.split(".", 2))

# str.splitlines([keepends])
# \n과 같은 줄 경계마다 문자열을 나누어 list로 반환
# keepends가 True로 주어지면 줄 경계 문자도 포함됨
str_a = "abc\ndef\n\nABC\nDEF\n"
print(str_a.splitlines())
print(str_a.splitlines(True))
# split과의 차이점
print(str_a.split("\n"))
print(str_a.splitlines())

# str.startswith(prefix[, start[, end]])
# prefix로 시작하는 문자열이 맞다면 True, 아니라면 False
# endswith()와 같이 작동

# str.strip([chars])
# 선행과 후행문자열 중 chars인 문자를 모두 제거하고 반환
# chars가 주어지지 않으면 공백을 제거하고 반환
str_a = "www.naver.com"
print(str_a.strip("wcom."))

# str.swapcase()
# 소문자는 대문자로, 대문자는 소문자로 바꾸어 반환
str_a = "Hello"
print(str_a.swapcase())
print(str_a.swapcase().swapcase())

# str.title()
# 단어의 첫 글자는 대문자, 나머지 문자는 소문자로 바꾸어 반환
str_a = "hello world"
print(str_a.title())

# a-zA-z를 제외한 것을 기준으로 단어라고 정의하기 때문에
# they're 같은 경우에는 They'Re로 나올 수 있음을 주의
# 정규식을 통해 해결할 수 있음
# >>> import re
# >>> def titlecase(s):
# ...     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
# ...                   lambda mo: mo.group(0).capitalize(),
# ...                   s)
# ...
# >>> titlecase("they're bill's friends.")
# "They're Bill's Friends."

# str.translate(table)
# 잘 모르겠음
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))
print(mytable)

# str.upper()
# 모든 문자를 대문자로 바꾸어 반환
str_a = "abc"
print(str_a.upper())

# str.zfill(width)
# 문자열의 왼쪽에서부터 "0"으로 채운 width만큼의 크기를 가진 문자열 반환
# 선행 부호 "+", "-"가 있는 경우에는 이 선행 부호가 맨 왼쪽으로 감

