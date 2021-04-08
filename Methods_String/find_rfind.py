# str.find(sub[, start[, end]] )
# 문자열의 왼쪽에서부터 처음 찾은 sub의 index를 반환한다.
# sub가 없는 경우, -1이 반환된다.
# start, end가 제공되는 경우, 범위를 지정할 수 있다.

a = "Let it be, let it be, let it be"
print(a.find("it"))
# 4
print(a.find("ayo"))
# -1

# str.rfind(sub[, start[, end]] )
# 문자열의 오른쪽에서부터 처음 찾은 sub의 index를 반환한다.
# sub가 없는 경우, -1이 반환된다.
# start, end가 제공되는 경우, 범위를 지정할 수 있다.

a = "Let it be, let it be, let it be"
print(a.rfind("it"))
# 26
print(a.rfind("ayo"))
# -1