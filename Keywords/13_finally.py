# finally
# try... execept가 끝나고 마지막에 사용하며, 항상 거친다.

def func(n):
    try:
        if n == 0:
            raise ZeroDivisionError
        r = 1/n
        return r
    except ZeroDivisionError:
        return "0으로는 못나눠요"
    finally:
        return "함수가 작동했어요"

print(func(0))
# 0으로는 못나눠요
# 함수가 작동했어요