# eval(expression[, globals[, locals]]) : evaluate
# expression arguments를 감정, 평가하여 값을 반환한다.
# expression는 string이나 bytes, code object여야 한다.
# globals는 제공되는 경우, dictionary여야 한다.
# locals 또한, 제공되는 경우에 모든 mapping object가 될 수 있다.
# 주의
# eval()는 실제 처리과정에서 과부하를 일으킬 수 있다.
# compile()을 통해 안전하게 사용할 필요가 있다.

# int object와 정수를 동시에 사용한 경우
a = 1
print(eval("a+1"))
# 2

# dictionary의 keys를 사용한 경우
b = dict(first="hello ", second="my ", third="deer ")
print(eval("first + second + third", b))

### 상세설명 ###

import builtins
from math import *

# 전역과 지역 범위를 둘 다 생략할 때
print(eval("dir()"))
# ['__annotations__', '__builtins__', ..., 'trunc', 'ulp']

# 전역 범위는 값을 주지만, 지역 범위는 생략할 때 (전역 범위에 {}를 넣어 값을 준 것으로 처리할 때)
# 'dir()'은 __builtins__안에 있어 사용 가능
print(eval('dir()', {}))
# ['__builtins__']

# sqrt()는 math module안에 있어 사용 불가능
# eval("sqrt(4)",{})
# # NameError: name 'sqrt' is not defined

# 사용 가능하게 만들기

# 전역 범위에 dictionary 선언
names = {"square_root" : sqrt, "power" : pow}
print(eval("dir()", names))
# ['__builtins__', 'power', 'square_root']

# 사용
print(eval("square_root(9)", names))
# 3.0

# built-ins 제한하기
# eval("dir()", {"__builtins__" : None})
# # TypeError: 'NoneType' object is not subscriptable
# eval("dir()", {"__builtins__" : {}})
# # NameError: name 'dir' is not defined

# 전역과 지역 범위에 둘 다 값을 줄 때
print(eval("ssqrt(a)", {"__builtins__" : None}, {'a' : 16, 'ssqrt' : sqrt}))
# = print(eval("ssqrt(a)", {'a' : 16, 'ssqrt' : sqrt}))
# 4.0