# type(object)
# type(name, bases, dict)
# class이며, argument가 하나인 경우, object의 type을 반환한다.
# arguments가 세 개인 경우, arguments에 따라 새 type의 object를 반환한다.
# name : class의 이름을 제공하면 된다.
# bases : base class를 항목화하는 tuple(__bases__ attribute)를 제공하면 된다.
# dict : class body에 대한 정의를 포함하는 namespace dictionary(__dict__ attribute)를 제공하면 된다.

# 사용해보자
# 출처 https://www.programiz.com/python-programming/methods/built-in/type

# argument가 하나인 경우
# list
numbers_list = [1, 2]
print(type(numbers_list))
# <class 'list'>

# dictionary
numbers_dict = {1: 'one', 2: 'two'}
print(type(numbers_dict))
# <class 'dict'>

# instance
class Foo:
    a = 0

foo = Foo()
print(type(foo))
# <class '__main__.Foo'>

# object의 type을 확인해야하는 경우, type() 대신에 isinstance() 함수를 사용하는 것이 좋다.
print(isinstance(foo, Foo))
# True

# name, bases, dict

# 이름은 'X', object이고, 내용은 a='Foo', b=12인 object
o1 = type('X', (object,), dict(a='Foo', b=12))
print(type(o1))
# <class 'type'>

# __dict__ attribute를 확인해보자
print(vars(o1))
# {'a': 'Foo', 'b': 12, '__module__': '__main__', ... , '__doc__': None}

# test라는 새 type을 만들고
class test:
  a = 'Foo'
  b = 12

# arguments를 넣어서 object를 만들자
o2 = type('Y', (test,), dict(a='Foo', b=12))
print(type(o2))
# <class 'type'>

# __dict__ attribute를 확인해보자
print(vars(o2))
# {'a': 'Foo', 'b': 12, '__module__': '__main__', '__doc__': None}

# 참고
# 필요한 경우, 이름을 바꿔줄 수 있다.
print(o1.__name__)
# X
o1.__name__ = 'Z'
print(o1.__name__)
# Z