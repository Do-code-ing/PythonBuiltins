# id(object)
# object의 'identity'를 반환한다.
# id는 object가 수명이 다 할 때까지 바뀌지 않는 정수다.
# 수명이 겹치지 않는 두 개의 objects는 같은 id 값을 가질 수 있다.
# int, str같은 단일 element를 가지는 type의 경우 element가 같다면 id 또한 같다.

# id가 같은 경우
num_a = 123
num_b = 123
print(id(num_a))
print(id(num_b))
# ex)2036090886320

str_a = "안녕"
str_b = "안녕"
print(id(str_a))
print(id(str_b))
# ex)2036096390704

float_a = 123.0
float_b = 123.000
print(id(float_a))
print(id(float_b))
# ex)2036096203792

# id가 다른 경우
list_a = [12,34,56]
list_b = [12,34,56]
print(id(list_a))
# ex)2036096430272
print(id(list_b))
# ex)2036096451520

set_a = {"hello":"hello","bye":"bye"}
set_b = {"hello":"hello","bye":"bye"}
print(id(set_a))
# ex)2036096064192
print(id(set_b))
# ex)2036096064384