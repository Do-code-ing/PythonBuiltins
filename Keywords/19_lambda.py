# lambda
# 이름이 없는 함수를 만드는 데 사용된다.
# return 문을 포함하지 않는 inline 함수다.
# 평가 및 반환되는 식으로 구성된다.

a = lambda x:x*2
for i in range(1,6):
    print(a(i))
# 2
# 4
# 6
# 8
# 10