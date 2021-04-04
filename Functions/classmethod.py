# 한국인 전용 공항
class EmigrationKor():
    def __init__(self, kor_name, kor_age, country):
        self.name = kor_name
        self.age = kor_age
        self.country = country
    
    def __str__(self):
        return f"이름 : {self.name}, 나이 : {self.age}, 국적 : {self.country}"

    def method1(self):
        pass

    def method2(self):
        pass

    def method3(self):
        pass

    def method4(self):
        pass

# 미국인 전용 공항
class EmigrationEng():
    def __init__(self, information):
        information = information.split(" ")
        self.name = "지미" if information[0] == "Jimmy" else f"{information[0]} (번역실패)"
        self.age = int(information[1])+1
        self.country = "미국" if information[2] == "America" else f"{information[2]} (번역실패)"
    
    def __str__(self):
        return f"이름 : {self.name}, 나이 : {self.age}, 국적 : {self.country}"

    def method1(self):
        pass

    def method2(self):
        pass

    def method3(self):
        pass

    def method4(self):
        pass

# 한국인이 한국 공항으로
이상민 = EmigrationKor("이상민", 27, "한국")
print(이상민)

# 한국인이 미국 공항으로
# 이상민 = EmigrationEng("Sangmin-Lee", 26, "Korea")
# print(이상민)
# 그러나 미국 공항과 한국 공항의 입국심사법이 달라서 에러 발생

# 미국 공항식으로 입국
이상민 = EmigrationEng("Sangmin-Lee 25 Korea")
print(이상민)

# 미국인이 한국 공항으로
# Jimmy = EmigrationKor("Jimmy 24 America")
# print(Jimmy)
# 그러나 미국 공항식으로 서류를 작성하여 불가

# 미국인이 미국 공항으로
Jimmy = EmigrationEng("Jimmy 24 America")
print(Jimmy)

# classmethod를 통해 한 공항에서 두 가지 방식으로 입국 가능하게 할 수 있다.
# classmethod는 값을 self가 아닌 cls로 받는 다는 차이점을 제외하곤 일반 class를 작성할 때 처럼 하면 된다.

# 공용 공항
class Emigration():
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
    
    def __str__(self):
        return f"이름 : {self.name}, 나이 : {self.age}, 국적 : {self.country}"

    # 직원들이 영어를 조금 배웠어요.
    @classmethod
    def emigration_eng(cls, eng):
        eng = eng.split(" ")
        name = "지미" if eng[0] == "Jimmy" else f"{eng[0]} (번역실패)"
        age = int(eng[1])+1
        country = "미국" if eng[2] == "America" else f"{eng[2]} (번역실패)"
        return cls(name, age, country)

    def method1(self):
        pass

    def method2(self):
        pass

    def method3(self):
        pass

    def method4(self):
        pass

# 한국인이 한국인 규정으로
이상민 = Emigration("이상민", 27, "한국")
print(이상민)

# 한국인이 미국인 규정으로
이상민 = Emigration.emigration_eng("Sangmin-Lee 26 Korea")
print(이상민)

# 미국인이 한국어 규정으로
# Jimmy = Emigration("Jimmy 24 America")
# print(Jimmy)

# 미국인이 미국어 규정으로
Jimmy = Emigration.emigration_eng("Jimmy 24 America")
print(Jimmy)

# 이처럼 classmethod를 통해 class를 더 만들 필요 없이 코드를 작성하여
# clean code로 만들어 코드의 양을 줄이며 보기 좋게 만들 수 있고, 코드 관리가 편해진다.

# classmethod와 staticmethod를 한 번에 사용하는 예제를 보고싶다면 staticmethod.py를 확인