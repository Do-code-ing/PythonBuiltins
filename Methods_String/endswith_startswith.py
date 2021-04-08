# str.endswith(suffix[, start[, end]])
# 문자열이 suffix로 끝나면 True, 아니라면 False를 반환한다.
# start, end가 제공되는 경우, 범위를 지정할 수 있다.

a = "Hello world."
print(a.endswith("world"))
# False
print(a.endswith("world."))
# True

# str.startswith(prefix[, start[, end]])
# 문자열이 prefix로 시작하면 True, 아니라면 False를 반환한다.
# start, end가 제공되는 경우, 범위를 지정할 수 있다.

a = "Hello world."
print(a.startswith("Hello"))
# True
print(a.startswith("ello"))
# False