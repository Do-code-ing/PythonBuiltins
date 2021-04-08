# break, continue
# for과 while loops에서 정상적인 동작을 변경하는 데 사용된다.
# break는 loop를 탈출한다.
# continue는 loop의 현재 반복을 탈출하지만 전체 loop는 탈출하지 않는다.

for i in range(10):
    if i == 5:
        break
    print(i)
# 0
# 1
# 2
# 3
# 4

for i in range(10):
    if i == 5:
        continue
    print(i)
# 0
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9