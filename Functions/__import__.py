# __import__(name, globals=None, locals=None, fromlist=(), level=0)
# import문에 의해 호출되는 함수다.
# name : import할 module의 이름을 제공하면 된다.
# globals & locals : name의 해석 방법을 결정한다.
# fromlist : name으로 가져와야하는 objects 또는 submodules를 제공하면 된다.
# level : 절대적 또는 상대적 imports를 할지 지정한다.

# 참고
# __import__() 함수는 일상적인 Python program에 필요하지 않다.
# 거의 사용되지 않으며, 종종 권장하지 않는다.
# 이 함수는 명령문이 이 함수를 호출할 때 import문의 의미를 변경하는데에 사용할 수 있다.
# 하지만 import hooks를 사용하는 것이 더 좋다.
# 그리고 name으로 module을 import하려면 importlib.import_module() 을 사용하면 된다.

# 사용해보자
# 출처 https://www.programiz.com/python-programming/methods/built-in/__import__

# 다음의 import를 통해 함수를 사용하는 것을 
import math

print(math.fabs(-2.5))
# 2.5

# 다음과 같이 사용할 수 있다.
mathematics = __import__('math', globals(), locals(), [], 0)
print(mathematics.fabs(-2.5))
# 2.5

# 사실 참고(line 8)처럼 다음과 같이 사용하는게 더 편한 것 같다.
import math as module_math

print(module_math.fabs(-2.5))
# 2.5