# string.casefold()
# 문자열내에 모든 문자를 소문자로 변환 후 반환한다.

a = "HELLO WORLD"
print(a.casefold())
# hello world

# lower()과의 차이점
# 영어가 아닌 경우
a = "der Fluß"
print(a.casefold())
# der fluss
print(a.lower())
# der fluß