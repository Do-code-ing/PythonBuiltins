# except, raise, try
# 예외 처리시 사용된다.
# 예외는 문제가 발생했음을 나타내는 error다.
# 예를 들어, IOError, ValueError, ZeroDivisionError 등이 있다.

def func(n):
    try:
        r = 1/n
    except:
        return "예외 처리"
    return r

print(func(10))
# 0.1
print(func(0))
# 예외 처리

# 예외 발생시키기
def func(n):
    try:
        if n == 0:
            raise ZeroDivisionError
        r = 1/n
    except ZeroDivisionError:
        return "0으로는 못나눠요"
    return r

print(func(0))
# 0으로는 못나눠요