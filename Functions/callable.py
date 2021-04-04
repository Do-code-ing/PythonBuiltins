# callable(object)
# object argument가 부를 수 있을 거 같으면 True, 아니면 False를 반환한다.
# True가 반환되면 object를 호출할 때 실패할 가능성이 있다.
# 왜냐하면 class는 항상 callable하기 때문이다.
# class object를 항상 호출하고 싶다면 class 작성 시 __call__() method를 사용하여 instance도 callable로 만들면 된다.
# False가 반환되면 object를 호출할 때 항상 실패한다.

# 아무거나 부를 때
print(callable(5))
# False

class Callable_1:
    def __init__(self, x):
        self.x = x

# class 자체를 부를 때
print(callable(Callable_1))
# True

# callable하지 않는 instance object를 부를 때
a = Callable_1(5)
print(callable(a))
# False

# callable하게 만들기
class Callable_2:
    def __init__(self, x):
        self.x = x
    
    def __call__(self):
        pass
    
# callable한 instance object를 부를 때
b = Callable_2(10)
print(callable(b))
# True