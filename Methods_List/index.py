# list.index(element, start, end)
# list에서 왼쪽부터 element가 몇 번째에 처음 등장하는지를 반환한다.
# start, end가 제공되는 경우, 범위를 지정할 수 있다.
# element가 list내에 없는 경우에는 'ValueError'가 발생한다.

lst = [1,2,3,4,1]
print(lst.index(1))
# 0
# 맨 첫 번째 index는 0이다.

print(lst.index(1, 1))
# 4
# index 1부터 찾아봤기 때문에 그 다음에 1이 등장하는 경우는 index 4

# print(lst.index(1, 1, 3))
# ValueError: 1 is not in list
# index 1 ~ 3 사이에는 1이 없기 때문에 ValueError 발생