# delattr(object, name) : delete attribute
# setattr()과 친척 관계다.
# object가 허용하는 경우 object가 가지고 있는 attribute 중 'name'인 것을 삭제한다.
# 예를 들어, 기본식인 delattr(object, 'name')은 del object.name과 같다.

class TalkTo:
    def __init__(self, name, someone):
        self.name = name
        self.someone = someone
    
    def hello(self):
        print(f"{self.name} say(s) \"hello\" to {self.someone}")

    def bye(self):
        print(f"{self.name} say(s) \"bye\" to {self.someone}")

# 현재 diretory 확인
print(dir(TalkTo))
# ['__class__', '__delattr__', ... , '__weakref__', 'bye', 'hello']

# 'hello' 삭제
delattr(TalkTo, "hello")
print(dir(TalkTo))
# ['__class__', '__delattr__', ... , '__weakref__', 'bye']

# 'bye' 삭제
del TalkTo.bye
print(dir(TalkTo))
# ['__class__', '__delattr__', ... , '__weakref__']

# getattr(object, name[,default])
# object의 attribute 중 'name'인 attribute를 돌려준다.
# 예를 들어, 기본식인 getattr(object, 'name'[,default])는 object.name과 같다.
# attribute가 없어 돌려줄 수 없는 경우, AttributeError가 발생하며, default를 제공하면 그 값이 반환된다.

class TalkTo:
    def __init__(self, name, someone):
        self.name = name
        self.someone = someone
    
    def hello(self):
        print(f"{self.name} say(s) \"hello\" to {self.someone}")

    def bye(self):
        print(f"{self.name} say(s) \"bye\" to {self.someone}")

talking = TalkTo("I", "You")

# class 자체에 'hello'에 대해
print(getattr(TalkTo, "hello"))
# <function TalkTo.hello at 0x000001DF419DF430>

# instance object에 'hello'에 대해
print(getattr(TalkTo("I", "You"), "hello"))
# <bound method TalkTo.hello of <__main__.TalkTo object at 0x000001DF419EEF70>>

# instance object에 해당 attribute에 대해 없으면 ':(' 출력
print(getattr(talking, "bye", ":("))
# <bound method TalkTo.bye of <__main__.TalkTo object at 0x000002D993C6DA00>>
print(getattr(talking, "None", ":("))
# :(

# setattr(object, name, value)
# getattr()와 부합한다.
# object의 attribute 중 'name'인 attribute에게 혹은, 'name'인 새 attribute를 지정할 수 있다.
# object가 허용하는 경우, value를 attribute에 대입한다.
# 예를 들어, 기본식인 setattr(object, 'name', value)는 object.name = value와 같다.

# 새 attribute 추가
setattr(TalkTo, "hello", "Here is new setted attribute!")
print(getattr(talking, "hello"))
# Here is new setted attribute!
setattr(TalkTo, "good morning", "Good morning :)")
print(getattr(TalkTo, "good morning"))
# Good morning :)