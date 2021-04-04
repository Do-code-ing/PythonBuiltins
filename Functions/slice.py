# slice(stop)
# slice(start, stop[, step])
# class이며, range(start, stop, step) 에 의해 지정된 index set를 나타내는 slice object를 반환한다.
# start : 자를 범위의 시작 (기본값 = None)
# stop : 자를 범위의 끝
# step : start에서 stop까지 몇 단계에 하나씩인지 반환할 건지 (기본값 = None)
# 참고
# slice_object = slice(1, 10, 1) 일 때,
# list[silce_object] 는 list[1:10:1] 또는 list[1:10, 1] 과 같다.

# 만들어보자
slice_a = slice(5)
print(slice_a)
# slice(None, 5, None)
slice_b = slice(1, 5, 2)
print(slice_b)
# slice(1, 5, 2)

# 반대 방향
slice_c = slice(-1, -4, -1)
print(slice_c)
# slice(-1, -4, -1)

# 사용해보자
str_a = "안녕하세요."
slice_str_a = str_a[slice_b]
print(slice_str_a)
# 녕세

# 반대 방향
str_b = "Python"
slice_str_b = str_b[slice_c]
print(slice_str_b)
# noh