# vars([object])
# module, class, instance 또는 __dict__ attribute가 있는 object의 __dict__ attribute를 반환한다.
# object에 __dict__ attribute가 없는 경우, 'TypeError'가 발생한다.
# argument가 없다면, locals() 처럼 동작한다.
# (참고로 지역 dictionary에 대한 변경이 무시되기 때문에 읽기에만 유용하다.)

# 사용해보자
# 출처 https://www.programiz.com/python-programming/methods/built-in/vars

# class를 하나 만들고
class Foo:
  def __init__(self, a, b):
    self.a = a
    self.b = b

object = Foo(5, 10)
print(vars(object))
# {'a': 5, 'b': 10}

# Python shell에서도 동작한다.
print(vars(list))
print(vars(str))
print(vars(dict))
# 출력 결과는 terminal에서 확인해보자

# 참고
# module 및 instance와 같은 object는 update 가능한 __dict__ attribute를 갖는다.
# 그러나, 다른 objects는 __dict__ attribute에 쓰기 제한을 가질 수 있다.
# (에를 들어, class는 직접적인 dictionary의 갱신을 받지 않기 위해 types.MappingProxyType을 사용한다.)