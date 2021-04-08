# str.strip([chars])
# 문자열에서 양 끝에서 chars에 해당하는 것을 지우고(해당하는게 없으면 멈춘다) 반환한다.
# chars가 주어지지 않으면 공백을 제거하고 반환한다.

str_a = "www.naver.com"
print(str_a.strip("wcom."))
# naver

# str.lstrip([chars])
# 문자열에서 왼쪽부터 chars에 해당하는 것을 지우고(해당하는게 없으면 멈춘다) 반환한다.
# chars가 주어지지 않으면 공백을 제거하고 반환한다.

str_a = "www.naver.com"
print(str_a.lstrip('.wa'))
# naver.com
print(str_a.removeprefix("www.")) # 왼쪽부터 해당하는 문자열 지우기
# naver.com

# str.rstrip([chars])
# lstrip()과 같으며 반대 방향으로 한다.
# chars가 주어지지 않으면 공백을 제거하고 반환한다.

str_a = "www.naver.com"
print(str_a.rstrip('.cmo'))
# www.naver
print(str_a.removesuffix(".com")) # 오른쪽부터 해당하는 문자열 지우기
# www.naver