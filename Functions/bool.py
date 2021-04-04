# bool([x]) : boolean
# class이며, [x] 값이 참, 거짓인지 파악하여 참이면 True, 거짓이면 False로 값 반환한다.
# None, 정수 0, 실수 0.0, 빈 문자열(공백은 True), 빈 리스트, 빈 집합 등은 False 이다. (나머지는 모두 True)

# 비교문이 있는 경우
x = 2 > 1
y = 1 > 2

print(bool(x))
# True
print(bool(y))
# False

# 문자열인 경우
print(bool(""))
# False
print(bool(" "))
# True
print(bool("뿌ㅖㄹㄲ뗽꼙"))
# True

# list인 경우
print(bool([]))
# False
print(bool(["hello","hi"]))
# True

# 집합인 경우
print(bool(set({})))
# False
print(bool(set({"hello","hi"})))
# True