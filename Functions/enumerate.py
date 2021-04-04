# enumerate(iterable, start=0)
# iterable arguments를 enumerate object로 반환한다.
# iterable에는 sequence, iterator, iteration을 지원하는 object여야 한다.
# enumerate()에 의해 반환된 iterator의 __next__() method는
# count(기본값 0을 갖는 start부터)와 iterable을 iteration해서 얻어지는 값을 포함하여 tuple로 반환한다.

# enmerate object 만들기
season = ["Sping", "Summer", "Fall", "Winter"]
print(enumerate(season))
# <enumerate object at 0x0000022DE057A5C0>

# object의 list
print(list(enumerate(season)))
#[(0, 'Sping'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

# start 값을 넣은 경우
print(list(enumerate(season, start=1)))
#[(1, 'Sping'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
season = enumerate(season, start=1)
print(next(season))
# (1, 'Sping')
print(next(season))
# (2, 'Summer')

# 참고
# def enumerate(sequence, start=0):
#     n = start
#     for elem in sequence:
#         yield n, elem
#         n += 1
