# str.maketrans(x[, y[, z]])
# str.translate()에 사용할 수 있는 translate table을 반환한다.
# argumnet가 1개인 경우,
# dictionary어야 하고, 단일 문자열간에 일 대 일로 매핑 또는 해당 번역으로의 유니코드 번호("a"는 97)이 포함되어야 한다.
# 2개인 경우,
# x와 y는 같은 길이의 문자열이어야 하며, x를 y로 대체한다.
# 3개인 경우,
# 3번 째 argument의 각 문자는 None으로 매핑된다.

# str.translate(table)
# translate table로 해당 문자열을 변환하여 반환한다.

# 출처 https://www.programiz.com/python-programming/methods/string/maketrans
# first string
firstString = "abc"
secondString = "ghi"
thirdString = "ab"

string = "abcdef"
print("Original string:", string)
# Original string: abcdef

translation = string.maketrans(firstString, secondString, thirdString)
print(translation)
# {97: None, 98: None, 99: 105}

# translate string
print("Translated string:", string.translate(translation))
# Translated string: idef

# first string
firstString = "abc"
secondString = "def"
thirdString = "abd"
string = "abc"
print(string.maketrans(firstString, secondString, thirdString))
print("".maketrans(firstString, secondString, thirdString))
# abc -> def
# {97: 100, 98: 101, 99: 102}
# except abd
# {97: None, 98: None, 99: 102, 100: None}