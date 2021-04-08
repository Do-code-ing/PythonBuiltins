# str.partition(sep)
# 문자열을 sep을 기준으로 (sep 앞의 문자열), (sep), (sep 뒤의 문자열)인 tuple로 반환한다.

str_a = "www.naver.com"
print(str_a.partition("."))
# ('www', '.', 'naver.com')

# str.rpartiton(sep)
# partition()에서 sep을 찾을 때 반대 순서로 찾아서 반환한다.

str_a = "www.naver.com"
print(str_a.rpartition("."))
# ('www.naver', '.', 'com')