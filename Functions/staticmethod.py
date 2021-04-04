# 덧셈 함수
def f_sum(x, y):
    return x + y

# 뺄셈 함수
def f_sub(x, y):
    return x - y

# 두 함수를 묶어 보관하기 위해 class를 사용할 수 있는데

class Sum1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def f_sum1(self):
        return self.x + self.y

    def f_sub1(self):
        return self.x - self.y

value = Sum1(3, 5)
print(value.f_sub1())
print(Sum1(6, 10).f_sub1())

# class는 기본적으로 __init__에 값(x, y)를 받아 instance object로 만들고 method를 작동 시키는데,
# staticmethod는 __init__ 값을 받을 필요가 없이, instance object를 생성하지 않으면서 함수를 사용할 수 있어,
# 메모리 확보 및 관리에 도움을 준다.

class Sum2:
    @staticmethod
    def f_sum2(x, y):
        return x + y

    @staticmethod
    def f_sub2(x, y):
        return x - y

print(Sum2.f_sub2(5,6))

# staticmethod는 class를 통해서만 사용할 수 있는 함수로,
# 마치 패키지나 모듈을 import하여 사용하는 듯한 효과를 낸다.
# 이는 사용자가 사용할 때 직관성이 생겨 코드의 내용을 따로 확인하지 않아도,
# 대략 어느 작업을 수행하는데 필요한 함수인지 알 수 있어 편리하다.
# 즉 비슷한 함수를 정리하여 넣어놓아 관리가 용이하고, clean code를 쓰는데에 도움이 된다.

# 응용
# staticmethod로 값을 받아오고, classmethod로 처리하여 instance object를 만들 수도 있다.

# [출처] [PYTHON] classmethod, staticmethod의 필요성|작성자 내이름은소영
# https://blog.naver.com/imbgirl/221589710333s

class student(object):
    def __init__(self, year, month, day, gender, name):
        self.year = year
        self.month = month
        self.day = day        
        self.gender = gender
        self.name = name
        
    def __str__(self):
        return f'{self.name}: {self.year}-{self.month:02d}-{self.day:02d} ({self.gender})'

    @staticmethod
    def splitID(ID):
        temp = int(ID[-1])        
        year = (2000 if temp > 2 else 1900) + int(ID[:2])
        month = int(ID[2:4])
        day = int(ID[4:6])
        gender = 'M' if temp % 2 else 'F'
        return [year, month, day, gender]
    
    @classmethod
    def fromID(cls, ID, name):
        return cls(*student.splitID(ID), name)

s = [2007, 11, 2, "F", "merry"]
a = student(*s)
#a = student(2007, 11, 2, "F", "merry")
print(a)

#b = student.fromID("0711024", "merry")
b = a.fromID("0711024", "merry")
print(b)

s = student.splitID("0711024")
c = student(*s, "merry")
print(c)