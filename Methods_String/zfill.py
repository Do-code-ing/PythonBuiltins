# str.zfill(width)
# 문자열의 왼쪽에서부터 "0"으로 채운 width만큼의 크기를 가진 문자열 반환한다.
# 선행 부호 "+", "-"가 있는 경우에는 이 선행 부호가 맨 왼쪽으로 간다.

a = "hello"
print(a.zfill(10))
# 00000hello

a = "+10"
print(a.zfill(10))
# +000000010