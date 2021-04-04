# range(stop)
# range(start, stop[, step])
# class이며, range type의 object를 반환한다.
# range(stop) 경우, start는 0이며, stop전 까지의 범위를 반환한다.
# start : 범위의 시작 (기본값 = 0)
# stop : 범위의 끝
# step : start에서 stop까지 몇 단계에 하나씩인지 반환할 건지 (기본값 = 1)

# stop만 있는 경우
range_a = range(5)
print(range_a)
# range(0, 5)
print(list(range_a))
# [0, 1, 2, 3, 4]

# start와 stop
range_b = range(5, 10)
print(range_b)
# range(5, 10)
print(list(range_b))
# [5, 6, 7, 8, 9]

# start, stop, step
range_c = range(5, 10, 2)
print(range_c)
# range(5, 10, 2)
print(list(range_c))
# [5, 7, 9]
# '5'부터 '10의 전'(=9)까지 2번에 하나씩 반환