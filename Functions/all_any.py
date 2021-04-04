# all(object)
# object의 elements가 모두 iterable하면 True, 아니라면 False를 반환한다.
# iterable objects에는 None, False, 0 을 제외한 list, set, tuple, string, range, set, dicionary, generator가 있다.

# 범위의 경우
a = range(1,21)
print(all(a))
# True

# tuple의 경우
b = 1,1,1
print(all(b))
# True
c = 0,1,1
print(all(c))
# False
# 정수 0이 있어 False 반환
d = True, "숫자야숫자", "g후해햏ㅎ"
print(all(d))
# True

# 정수 0으로만 이루어진 경우
f = 0,0,0
print(all(f))
# False

# any(object)
# 객체의 element가 하나라도 iterable하면 True, 하나도 없으면 False를 반환한다.

# 범위의 경우
print(any(a))
# True
print(any(c))
# True
print(any(f))
# False