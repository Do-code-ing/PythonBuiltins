# exec(object[, globals[, locals]]) : execute
# object arguments를 실행[수행, 동작]하여 값을 반환한다.
# object는 string이나 bytes, code object여야 한다.
# globals는 제공되는 경우, dictionary여야 한다.
# locals 또한, 제공되는 경우에 모든 mapping object가 될 수 있다.
# 참고
# module 수준에서는 globals와 locals는 같은 dictionary이다.
# 주의
# exec()는 실제 처리과정에서 과부하를 일으킬 수 있다.
# compile()을 통해 안전하게 사용할 필요가 있다.

# 문자열인 경우
a = 3
code_a = "b = a*10\nprint(b)"
exec(code_a)
# 30

# eval()와 비슷하지만 살짝 다르다.
# exec("print(dir())")
# = print(eval("dir()"))
# ['__annotations__', '__builtins__' , ... ]

# 돌려줄 값이 없으면 None을 돌려준다.
print(exec("123"))
# None
# 그렇기 때문에 함수 정의 외부에서 return 및 yield 문을 사용할 수 없다.

### 상세 설명 ###

from math import *

# 전역과 지역 범위 둘 다 생략할 때
exec("print(dir())")
# ['__annotations__', '__builtins__', ... ]

# 전역 범위는 값을 주지만, 지역 범위는 생략할 때 (전역 범위에 {}를 넣어 값을 준 것으로 처리할 때)
# dir()은 __builtins__안에 있어 사용 가능
exec("print(dir())", {})
# ['__builtins__']

# sqrt() math module에 있어 사용 불가능
# exec("print(sqrt(9))", {})
# # NameError: name 'sqrt' is not defined

# 사용 가능하게 만들기
exec("print(dir())", {"sqrt": sqrt, "pow": pow})
# ['__builtins__', 'pow', 'sqrt']
exec("print(sqrt(9))", {"sqrt": sqrt, "pow": pow})
# 3.0

# 이름 바꿔서 사용해보기
exec("print(dir())", {"squareRoot": sqrt, "pow": pow})
# ['__builtins__', 'pow', 'squareRoot']
exec("print(squareRoot(9))", {"squareRoot": sqrt, "pow": pow})
# 3.0

# built-ins 제한하기
# exec(object, {"__builtins__": None})
# # TypeError: exec() arg 1 must be a string, bytes or code object

# 전역과 지역 범위에 둘 다 값을 줄 때
globalsParameter = {"__builtins__" : None}
localsParameter = {"print" : print, "dir" : dir}
exec("print(dir())", globalsParameter, localsParameter)
# ['dir', 'print']