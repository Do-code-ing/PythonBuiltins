# assert
# 디버깅 목적으로 사용한다.
# assert 뒤에 조건이 나오는데, 그 조건이 참이라면 아무 일도 일어나지 않지만,
# 조건이 거짓이라면 'AssertionError'가 발생한다.

a = 4
assert a < 5
# assert a > 5
# AssertionError

# 다음과 같이 메세지를 제공할 수도 있다.

# assert a > 5, "a의 값이 너무 작아요."
# AssertionError: a의 값이 너무 작아요.

# if not a > 5:
#   raise AssertionError("a의 값이 너무 작아요.")
# 와 같다.