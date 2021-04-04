# object
# class이며, 새 기능이 없는 object를 반환한다.
# object는 모든 class의 base class다.
# 모든 python classes의 instances에 공통적인 methods를 가지고 있다.
# 이 함수는 arguments가 필요없다.

# object 만들기
something = object()
print(something)
# <object object at 0x000001CC98C881B0>

# 놀랍게도 이 object의 type은 object입니다. 😮
print(type(something))
# <class 'object'>