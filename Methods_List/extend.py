# list.extend(iterable)
# list의 마지막 부분에 iterable를 추가한다.

lst = [1,2,3,4]
lst2 = [5,6,7,8]
lst.extend(lst2)
print(lst)
# [1, 2, 3, 4, 5, 6, 7, 8]

# 다음과 같은 방법으로도 extend 할 수 있다.
lst = [1,2,3,4]
lst2 = [5,6,7,8]
lst += lst2
print(lst)
# [1, 2, 3, 4, 5, 6, 7, 8]

lst = [1,2,3,4]
lst2 = [5,6,7,8]
lst[len(lst):] = lst2
print(lst)
# [1, 2, 3, 4, 5, 6, 7, 8]


# append()와의 차이점
lst = [1,2,3,4]
lst2 = [5,6,7,8]
lst.append(lst2)
print(lst)
# [1, 2, 3, 4, [5, 6, 7, 8]]