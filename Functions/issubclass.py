# issubclass(class, classinfo)
# class가 classinfo의 (직간접적인 혹은 가상의)subclass라면 True를 반환한다.
# class는 class 자체의 subclass로 간주한다.
# classinfo는 class objects로 이루어진 tuple일 수 있는데,
# 이 경우 classinfo의 모든 항목이 검사된다.
# 다른 모든 경우라면 False를 반환한다.

class SuperClass:
    def __init__(self):
        pass

class SubClass(SuperClass):
    def __init__(self):
        SuperClass.__init__(self)

class NotSubClass:
    def __init__(self):
        pass
    
# SubClass가 SuperClass의 subclass인지
print(issubclass(SubClass, SuperClass))
# True

# 그 반대의 경우
print(issubclass(SuperClass, SubClass))
# False

# NotSubClass가 SuperClass의 subclass인지
print(issubclass(NotSubClass, SuperClass))
# False

# tuple에 담아 확인
tuple_a = SubClass
print(issubclass(tuple_a, SuperClass))
# True

# instance object가 subclass인지
instance_a = SubClass()
# print(issubclass(instance_a, SuperClass))
# TypeError: issubclass() arg 1 must be a class
# instance object는 class가 아니라 안됨