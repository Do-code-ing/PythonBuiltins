# if, else, elif (elif : else if)
# 조건부 분기 또는 의사 결정에 사용된다.
# 조건이 참일 때만 사용하려면 if와 elif를,
# 거짓인 경우도 사용하려면 else를 사용하면 된다.

def if_example(a):
    if a == 1:
        return "One"
    elif a == 2:
        return "Two"
    else:
        return "Something else"

print(if_example(2))
# Two
print(if_example(4))
# Something else
print(if_example(1))
# One