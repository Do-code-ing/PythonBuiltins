# dict.fromkeys(sequence[, value])
# 새 dictionary를 반환하는데, sequence를 keys로 받고 value가 제공될 경우 그 값을 value로 한다.

lst = [1,2,3,4,5]
a = dict.fromkeys(lst)
print(a)
# {1: None, 2: None, 3: None, 4: None, 5: None}
value = ["V"]
a = dict.fromkeys(lst, value)
print(a)
# {1: ['V'], 2: ['V'], 3: ['V'], 4: ['V'], 5: ['V']}

# 다음과 같이 value를 update해서 dictionary의 value를 수정할 수 있다.
value.append("+")
print(a)
# {1: ['V', '+'], 2: ['V', '+'], 3: ['V', '+'], 4: ['V', '+'], 5: ['V', '+']}

# 다음과 같이 하면 영향을 주지 않게된다.
lst2 = [1,2,3,4,5]
value2 = ["v"]
b = {key : list(value2) for key in lst2}
# list(value2)를 value로 취함으로써 value2의 값이 바뀌어도 b는 영향을 받지 않게된다.
print(b)
value2.append("+")
print(b)