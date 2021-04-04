# help([object])
# 내장 도움말 시스템을 호출한다.
# argument가 제공되지 않으면, interpreter console에서 대화형 도움말 시스템이 시작된다.
# argument가 문자열이면, 문자열의 이름을 가진 module, function, class, method, keywoerd, documentation topic이 조회되고,
# 도움말 페이지가 console에 출력된다.
# argument가 object라면 object에 대한 도움말 페이지가 출력된다.

help()
# Welcome to Python 3.9's help utility!
# ...
# help>
# 찾아보고 싶은 것을 입력하면 됨

# 아무 문자열이나 입력한 경우
name = "Sang-Min"
help(name)
# No Python documentation found for 'Sang-Min'.
# Use help() to get the interactive help utility.
# Use help(str) for help on the str class.
# 'Sang-Min' 이라는 문서가 없으니 다른 방식을 사용하라고 알려줌

# 문자열인 'str' 을 입력한 경우
help("str")
# class str(object)
#  |  str(object='') -> str
#  |  str(bytes_or_buffer[, encoding[, errors]]) -> str
#  ...
# -- More  --
# 'str' 이라는 이름을 가진 class를 찾아 알려줌
# help(str) 과 같은 결과

class Some:
    def __init__(self, name):
        self.name = name

# class 를 입력한 경우
help(Some)
# class Some(builtins.object)
#  |  Some(name)
#  |
#  |  Methods defined here:
# ...
# -- More  --
# 해당 class 내부에 있는 정보를 알려줌

# instance object 를 입력한 경우
someone = Some("Sang-Min")
help(someone)
# class Some(builtins.object)
#  |  Some(name)
#  |
#  |  Methods defined here:
# ...
# -- More  --
# class를 입력한 값과 같은 결과를 보여주는듯 함

# method 를 입력한 경우
from random import *

help(randint)
# Help on method randint in module random:

# randint(a, b) method of random.Random instance
#     Return random integer in range [a, b], including both end points.
# 해당 method의 사용법을 알려줌