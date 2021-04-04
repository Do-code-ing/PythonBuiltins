# max(iterable, *[,key, default])
# max(arg1, arg2, *args[, key])
# iterable에서 가장 큰 항목이나 두 개 이상 arguments 중 가장 큰 것을 반환한다.
# line 1 : 하나의 positional argument가 제공되면, 그것은 iterable이어야 한다. 
# line 2 : 두 개 이상의 positional arguments가 제공되면, positional arguments 중 가장 큰 것을 반환한다. 
# key는 특정 key에 대한 value를 비교할 때 사용한다. (line 26)
# defualt는 arguments에 iterable이 없는 경우 반환받을 값을 넣으면 된다. (line 45)


# argument가 하나인 경우

# 문자열(알파벳 중 가장 뒷 순번의 것 반환)
iter_a = "hello my dear"
print(max(iter_a))
# y

# list
iter_b = ["hello", "all", "my", "friends"]
print(max(iter_b))
# my

# tuple
iter_c = 1,2,3
print(max(iter_c))
# 3

# dicitonary의 경우 max() 는 가장 큰 key를 반환한다.
iter_d = {"1":"a", "2":"b", "-1":"c", "-2": "d"}
print(max(iter_d))
# 2
# 가장 큰 value를 반환받기 위해서는 key parameter를 사용하면 된다.
max_a = max(iter_d, key=lambda x:iter_d[x])
print(max_a)
# -2
print(iter_d[max_a])
# d

# argument가 두 개 이상인 경우
object_a = 3
object_b = 6
object_c = 10
print(max(object_a, object_b, object_c))
# 10

# default
lst = []
print(max(lst, default=None))
# None

# min(iterable, *[,key, default])
# min(arg1, arg2, *args[, key])
# iterable에서 가장 작은 항목이나 두 개 이상 arguments 중 가장 작은 것을 반환한다.
# line 1 : 하나의 positional argument가 제공되면, 그것은 iterable이어야 한다. 
# line 2 : 두 개 이상의 positional arguments가 제공되면, positional arguments 중 가장 작은 것을 반환한다. 
# key는 특정 key에 대한 value를 비교할 때 사용한다. (line 26)
# defualt는 arguments에 iterable이 없는 경우 반환받을 값을 넣으면 된다. (line 45)
# 사용법은 max() 와 같다. 그러므로 예시는 pass하도록 하겠다.