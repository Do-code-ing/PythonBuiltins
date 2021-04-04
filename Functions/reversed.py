# reversed(seq)
# sequence의 역 iterator를 반환한다.
# sequence는 __reversed()__ method를 가지고 있거나,
# sequence protocol(__len__() method와 __getitem__() method)를 지원하는 object여야 한다.
# 예를 들어, tuple, list string, range 등이 있다.

# 사용해보자
# 출처 https://www.programiz.com/python-programming/methods/built-in/reversed

# 문자열
seq_string = 'Python'
print(list(reversed(seq_string)))
# ['n', 'o', 'h', 't', 'y', 'P']

# tuple
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seq_tuple)))
# ['n', 'o', 'h', 't', 'y', 'P']

# range
seq_range = range(5, 9)
print(list(reversed(seq_range)))
# [8, 7, 6, 5]

# list
seq_list = [1, 2, 4, 3, 5]
print(list(reversed(seq_list)))
# [5, 3, 4, 2, 1]

# custom objects
class Vowels:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __reversed__(self):
        return reversed(self.vowels)

v = Vowels()
print(list(reversed(v)))
# ['u', 'o', 'i', 'e', 'a']