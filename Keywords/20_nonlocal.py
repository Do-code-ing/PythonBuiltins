# nonlocal
# global과 유사하게 사용하는데,
# 함수안에 함수가 있는 경우, 두 지역이 생기는데,
# 깊은 지역에서 얕은 지역의 변수를 사용하려 할 때 사용할 수 있다.

def shallow():
    a = 5
    def deep():
        nonlocal a
        a = 10
        print("deep :", a)
    deep()
    print("shallow :", a)

print(shallow())
# deep : 10
# shallow : 10
# None

# nonlocal을 사용하지 않은 경우
def shallow():
    a = 5
    def deep():
        a = 10
        print("deep :", a)
    deep()
    print("shallow :", a)

print(shallow())
# deep : 10
# shallow : 5
# None