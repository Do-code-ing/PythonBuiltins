# map(function, iterable, ...)
# iterable의 모든 항목에 function을 적용한 후 그 결과를 반환하는 iterator를 반환한다.
# iterable arguments가 추가되면,
# function은 그 수 만큼 arguments를 받아들여야 하고 모든 iterable에서 병렬로 제공되는 항목들에 적용된다.
# 다중 iterables의 경우, iterator는 가장 짧은 iterable이 소모되면 멈춘다.

# argument가 하나인 경우
gener_a = (i for i in range(0, 5))
map_a = map(lambda x:x, gener_a)
print(map_a)
# <map object at 0x00000287F4779FD0>
lst_a = list(map_a)
print(lst_a)
# [0, 1, 2, 3, 4]

# argument가 추가되는 경우
gener_b_1 = (i for i in range(5, 9))
gener_b_2 = (i for i in range(5, 9))
func_a = lambda x, y:x+y
map_b = map(func_a, gener_b_1, gener_b_2)
print(map_b)
# <map object at 0x00000287F4779FA0>
lst_b = list(map_b)
print(lst_b)
# [10, 12, 14, 16]





