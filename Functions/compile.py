# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
# source를 편집하거나 번역하여 code나 AST object로 만든다.
# eval, exec을 호출할 때, 실제 처리과정에서 과부하를 줄 수 있기에 compile을 사용
# source : 문자열이나, bytes, AST object여야 한다.
# filename : code를 읽은 file 이름을 제공하면 된다.
#            code가 문자열이라면 <string>을 제공하면 된다.
# mode : compile하려는 code 종류를 지정하면 된다.
#        예를 들어, source가 문장의 sequence로 구성되어 있다면 'exec',
#                                 단일 표현식으로 구성되어 있다면 'eval',
#                                 단일 대화형으로 구성되어 있다면 'single'.
#        마지막 "single"의 경우, 표현식이 None을 제외한 값을 평가하여 print된다.
# flags, dont_inherit : source를 compile할 때 'future statements'가 어떠한 영향을 미치는지 제어한다.
#                       기본값 = 0
# optimize : compiler의 최적화 수준을 지정한다.
#            기본값 = -1

# 조금 더 자세한 내용을 알고 싶다면 아래의 주소에 들어가 보도록 하자.
# https://docs.python.org/ko/3/library/functions.html#compile
# https://www.programiz.com/python-programming/methods/built-in/compile

import ast

statement_a = "int_a + 3"
statement_b = "result = int_a + 3"
int_a = 10
statement_c = open(".\\study_builtins\\compile_doc.py")
filename_a = "<string>"

# 기본값으로 compile
print(compile(statement_a, filename_a, "eval"))
# <code object <module> at 0x00000261660065B0, file "<string>", line 1>
print(compile(statement_b, "statement_b", "single"))
# <code object <module> at 0x00000261660065B0, file "statement_b", line 1>
print(compile(statement_c.read(), "formula_doc", "exec"))
# <code object <module> at 0x00000261660065B0, file "formula_doc", line 1>

# compiler options과 future features, optimize를 넣어 compile
print(compile(statement_a, filename_a, "exec", ast.PyCF_ALLOW_TOP_LEVEL_AWAIT, 0, 2))
# <code object <module> at 0x00000261660065B0, file "<string>", line 1>

# 참고
# 'single' 또는 'eval' mode로 여러 줄 코드를 가진 문자열을 컴파일할 때,
# 적어도 하나의 개행 문자로 입력을 끝내야 한다.
# 이것은 code 모듈에서 문장이 불완전한지 완전한지를 쉽게 탐지하게 하기 위함이다.

# 경고
# 파이썬의 AST compiler에서 스택 깊이 제한으로 인해,
# AST object로 compile할 때 충분히 크고 복잡한 문자열로 인해 python interpreter가 crash를 일으킬 수 있다.