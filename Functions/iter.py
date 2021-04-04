# iter(object[, sentinel]) : iterator
# iterator object를 반환한다.
# sentinel이 주어질 경우 object는 callable해야 하는데,
# 이 경우 __next__() method가 호출될 때 마다 arguments없이 object를 호출한다.
# next() 를 통해 반환된 value와 sentinel이 같다면 'StopIteration'이 발생하고, 그렇지 않으면 value를 돌려준다.
# 즉 sentinel까지만 읽을 수 있다는 말이다.
# sentinel이 주어질 때, 유용하게 쓰일 수 있는 경우에는
# 예를 들어, 어떠한 file을 읽을 때, 읽고 싶은 범위를 제한하는 것이 있다.

# str object의 경우
str_a = "A"
iter_a = iter(str_a)
print(iter_a)
# <str_iterator object at 0x000002A5081EEFD0>

# tuple object의 경우
tuple_b = "A", "B"
iter_b = iter(tuple_b)
print(iter_b)
# <tuple_iterator object at 0x000002A5081EEEB0>

# sentinel이 주어질 경우

# class의 경우
class Call:
    def __init__(self):
        pass

    def __call__(self):
        return 1

iter_c = iter(Call, 1)
print(iter_c)
# <callable_iterator object at 0x00000123786FBB20>
print(next(iter_c))
# <__main__.Call object at 0x00000123786FBAC0>

# sentinel과 반환된 value가 다른 instance object의 경우
instance_d = Call()
iter_d = iter(instance_d, 2)
print(iter_d)
# <callable_iterator object at 0x00000123786FBA30>
print(next(iter_d))
# 1

# sentinel과 반환된 value가 같은 instance object의 경우
instance_e = Call()
iter_e = iter(instance_e, 1)
print(iter_e)
# <callable_iterator object at 0x00000123786FB970>
# print(next(iter_e))
# StopIteration