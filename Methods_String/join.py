# string.join(iterable)
# 문자열을 iterable의 elements 사이에 결합하여 반환한다.

# list
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))
# 1, 2, 3, 4

# tuple
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))
# 1, 2, 3, 4

s1 = 'abc'
s2 = '123'

# s1을 s2에 join하는 경우
print(s1.join(s2))
# 1abc2abc3
# '1'+ 'abc'+ '2'+ 'abc'+ '3'

# s2를 s1에 join하는 경우
print(s2.join(s1))
# a123b123c
# 'a'+ '123'+ 'b'+ '123'+ 'b'

# set
test = {'2', '1', '3'}
s = ', '
print(s.join(test))
# 1, 2, 3

test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))
# Python->->Java->->Ruby

# dict
test = {'mat': 1, 'that': 2}
s = '->'
print(s.join(test))
# mat->that

test = {1: 'mat', 2: 'that'}
s = ', '
# print(s.join(test))
# key가 문자열이 아닌 경우, 'TypeError'가 발생한다.