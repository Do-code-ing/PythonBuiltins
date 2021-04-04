# zip(*iterables)
# 각 iterable의 elements를 모으는 iterator를 만들어 반환한다.
# arguments가 없다면, 빈 iterator를 반환한다.
# arguments가 하나 이상이라면, 모든 iterable의 elements를 포함하는 각 tuple이 있는 tuples iterator를 반환한다.

# 사용해보자
# 출처 https://www.programiz.com/python-programming/methods/built-in/zip

# list를 만들고
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# arguments가 없다면, list로 만들어 출력해보자
result = zip()
result_list = list(result)
print(result_list)
# []

# 두 개의 iterables, set으로 만들어 출력해보자
result = zip(number_list, str_list)
result_set = set(result)
print(result_set)
# {(3, 'three'), (1, 'one'), (2, 'two')}

# iterable elements 갯수가 다른 경우
numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# 3개와 4개, set으로 만들어 출력
result = zip(numbersList, numbers_tuple)
result_set = set(result)
print(result_set)
# {(2, 'TWO'), (1, 'ONE'), (3, 'THREE')}

# 3개와 2개, 그리고 4개, set으로 만들어 출력
result = zip(numbersList, str_list, numbers_tuple)
result_set = set(result)
print(result_set)
# {(2, 'two', 'TWO'), (1, 'one', 'ONE')}
# 제일 적은 갯수를 가진 것을 기준으로 만들어 반환함

# unzip (zip되어 있는것을 풀기)
# list를 만들고
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

# zip 해주고
result = zip(coordinate, value)
result_list = list(result)
print(result_list)
# [('x', 3), ('y', 4), ('z', 5)]

# zip(*zipped) 를 통해 나눠준다.
c, v =  zip(*result_list)
print('c =', c)
print('v =', v)
# c = ('x', 'y', 'z')
# v = (3, 4, 5)