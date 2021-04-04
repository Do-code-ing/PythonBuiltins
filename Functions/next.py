# next(iterator[, default])
# __next__() method를 호출해 iterator에서 다음 항목을 꺼낸다.
# default가 주어지면, iterator가 고갈될 때 반환하고, 그렇지 않으면 'StopIteration'이 발생한다.

gener_a = (i for i in range(5))
print(next(gener_a, "It's over."))
# 0
print(next(gener_a, "It's over."))
# 1
print(next(gener_a, "It's over."))
# 2
print(next(gener_a, "It's over."))
# 3
print(next(gener_a, "It's over."))
# 4
print(next(gener_a, "It's over."))
# It's over.