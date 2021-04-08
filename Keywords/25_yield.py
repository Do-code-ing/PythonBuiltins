# yield
# return 문과 같이 사용된다. 그러나 generator를 반환한다.
# generator는 한 번에 하나의 항목을 생성하는 iterator다.
# 값이 큰 목록은 많은 메모리를 차지한다.
# generator는 모든 값을 메모리에 저장하는 대신, 한 번에 하나의 값만 생성하므로 이 상황에서 유용하다.

g = (2**x for x in range(100))
print(next(g))
# 1
print(next(g))
# 2
print(next(g))
# 4
print(next(g))
# 8
print(next(g))
# 16

# 이 유형의 generator는 함수의 yield 문에 의해 반환된다.

def generator():
    for i in range(6):
        yield i*i

g = generator()
for i in g:
    print(i)
# 0
# 1
# 4
# 9
# 16
# 25