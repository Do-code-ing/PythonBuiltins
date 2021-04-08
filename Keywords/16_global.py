# global
# 함수나 class 안에서, 즉 지역에서 전역 변수를 사용하기 위해 선언하는 문이다.

gun = 10

def loc_using(n):
    gun -= n

# loc_using(3)
# UnboundLocalError: local variable 'gun' referenced before assignment
# 지역 변수 중에 gun이 없어서 안된단다.
# 그래서 다음과 같이 전역 변수로 선언해주어야 한다.

def glo_using(n):
    global gun
    gun -= n

glo_using(3)
print(gun)
# 7