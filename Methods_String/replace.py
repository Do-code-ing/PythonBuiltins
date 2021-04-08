# str.replace(old, new[, count])
# 문자열 내의 모든 old 문자를 new 문자로 바꾸고, count가 있으면 count개의 문자만 바꾸고 반환한다.

str_a = "www.naver.com"
print(str_a.replace("naver.com", "daum.net"))
# www.daum.net

str_b = "abcaaabc"
print(str_b.replace("a", "A", 3))
# AbcAAabc