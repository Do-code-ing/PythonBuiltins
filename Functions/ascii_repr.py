# ascii(object) 
# object를 ASCII 코드로 인쇄가능한 형태로 반환한다.
# repr과 비슷하지만 비 ASCII문자는 탈출한다.

lst = list(i for i in range(0,3)), "\\", "한글", 1 , "<"
print(ascii(lst))
# ([0, 1, 2], '\\', '\ud55c\uae00', 1, '<')

# repr(object) : represent
# object를 인쇄가능한 형태로 반환한다.
# class 내부에 __repr__() method를 정의해 instance가 돌려받을 repr 값을 제어할 수 있다.

print(repr(lst))
# ([0, 1, 2], '\\', '한글', 1, '<')

class String:
    def __init__(self, x):
        self.x = x
        
    def __str__(self):
        return str(self.x)

    # repr() 로 반환받을 값 설정
    def __repr__(self):
        return str(id(self.x))


print(String(lst))
# ([0, 1, 2], '\\', '한글', 1, '<')
print(repr(String(lst)))
# 2230854869056

# 참고
# eval()에 전달될 때 같은 값을 가진 객체를 생성하는 문자열을 반환하려고 시도한다.
# 반환에 실패했다면 해당 object가 type과 name, address를 포함하는 추가의 정보를 <information> 형태이기 때문이다.
# ex) <map object at 0x00..>