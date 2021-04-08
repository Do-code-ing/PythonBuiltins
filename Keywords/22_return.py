# retrun
# 함수 내에서 종료하고 값을 반환하는데 사용된다.
# 명시적으로 값을 반환하지 않으면 None이 자동으로 반환된다.

def yes_return():
    a = 10
    return a

def no_return():
    a = 10

print(yes_return())
# 10
print(no_return())
# None