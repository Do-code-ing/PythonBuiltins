# str.split(sep=None, maxsplit=-1)
# 문자열을 sep을 기준으로 나누어 list로 반환한다.
# sep이 주어지지 않는다면 공백 문자를 기준으로 반환한다.
# maxsplit이 주어지면 그 숫자만큼만 반복한다.

str_a = "www.naver.com"
print(str_a.split(".", 2))
# ['www', 'naver', 'com']
print(str_a.split(".", 1))
# ['www', 'naver.com']

# str.rsplit(sep=None, maxsplit=-1)
# split()과 같으며 반대 방향으로 한다.

str_a = "www.naver.com"
print(str_a.rsplit(".", 1))
# ['www.naver', 'com']

# str.splitlines([keepends])
# 문자열을 \n과 같은 줄 경계마다 나누어 list로 반환한다.
# keepends가 True로 주어지면 줄 경계 문자도 포함된다.

str_a = "abc\ndef\n\nABC\nDEF\n"
print(str_a.splitlines())
# ['abc', 'def', '', 'ABC', 'DEF']

print(str_a.splitlines(True))
# ['abc\n', 'def\n', '\n', 'ABC\n', 'DEF\n']

# split과의 차이점
print(str_a.split("\n"))
# ['abc', 'def', '', 'ABC', 'DEF', '']

print(str_a.splitlines())
# ['abc', 'def', '', 'ABC', 'DEF']