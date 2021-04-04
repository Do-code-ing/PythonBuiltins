# property(fget=None, fset=None, fdel=None, doc=None)
# class이며, property attribute를 돌려준다.
# fget : attribute value를 가져오는 함수를 제공하면 된다.
#        기본값 = None
# fset : attribute value를 설정하는 함수를 제공하면 된다.
#        기본값 = None
# fdel : attribute value를 삭제하는 함수를 제공하면 된다.
#        기본값 = None
# doc : attribute에 대한 문서(docstring)이 포함되는 문자열이다.
#       기본값 = None

# arguments가 없을 때
print(property())
# <property object at 0x000001D8CB5E1590>
# 기본 property attribute를 반환한다.

# 사용해보자
# 출처 https://www.programiz.com/python-programming/methods/built-in/property
class Person:
    def __init__(self, name):
        self._name = name
    
    # fget 함수 만들기
    def get_name(self):
        print('Getting name')
        return self._name
    
    # fset 함수 만들기
    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value
    
    # fdel 함수 만들기
    def del_name(self):
        print('Deleting name')
        del self._name
    
    # property attribute 돌려받기
    # 세 가지 method를 property() 를 호출하여 설정
    name = property(get_name, set_name, del_name, 'Name property')

# 먼저 instance object를 만들고
p = Person('Adam')

# self.fget
print(p.name)
# Getting name
# Adam

# self.fset
p.name = 'John'
# Setting name to Jhon

# self.fdel
del p.name
# Deleting name

# 조금 더 이쁘게 사용하기
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Getting name')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name

# @property 를 사용해 함수 'name'을 fget으로 만든다
# 이 경우 getter method 전에 @property를 사용하여 수행된다.
# @name.setter 를 사용해 property의 두 번째 argument인 fset으로 만든다.
# 마찬가지로, @name.deleter 를 사용해 fdel로 만든다.