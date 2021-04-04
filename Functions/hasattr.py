# hasattr(object, name)
# name(string)이 object의 attributes 중 하나의 이름이라면 True,
#                                       아니라면 False 를 반환한다.
# 실제 처리과정은 getattr(object, name) 을 호출하고 'AttributeError'가 발생하는지를 본다.

class TalkTo:
    def __init__(self, name, someone):
        self.name = name
        self.someone = someone
    
    def hello(self):
        print(f"{self.name} say(s) \"hello\" to {self.someone}")

    def bye(self):
        print(f"{self.name} say(s) \"bye\" to {self.someone}")

# class에 해당 attribute가 있는지
print(hasattr(TalkTo, "hello"))
# True
print(hasattr(TalkTo, "bye"))
# True
print(hasattr(TalkTo, "None"))
# False