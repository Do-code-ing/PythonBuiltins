# str.index(sub[, start[, end]] )
# 문자열의 왼쪽에서부터 처음 찾은 sub의 index를 반환한다.
# sub가 없는 경우, 'ValueError'가 발생한다.
# start, end가 제공되는 경우, 범위를 지정할 수 있다.

a = "Let it be, let it be, let it be"
print(a.index("it"))
# 4
# print(a.index("ayo"))
# ValueError: substring not found

# str.rndex(sub[, start[, end]] )
# 문자열의 오른쪽에서부터 처음 찾은 sub의 index를 반환한다.
# sub가 없는 경우, 'ValueError'가 발생한다.
# start, end가 제공되는 경우, 범위를 지정할 수 있다.

a = "Let it be, let it be, let it be"
print(a.rindex("it"))
# 26
# print(a.rindex("ayo"))
# ValueError: substring not found