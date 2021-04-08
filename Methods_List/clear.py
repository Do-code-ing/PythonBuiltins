# list.clear()
# list의 모든 items를 삭제한다.

lst = [1,2,3,4]
lst.clear()
print(lst)
# []

# del을 사용해 삭제할 수도 있다.
lst = [1,2,3,4]
del lst[:]
print(lst)
# []
# del lst의 경우 lst 자체를 삭제하지만,
# del lst[:]의 경우 lst의 처음부터 끝까지라는 범위를 지정해주었기 때문에 items만 삭제한다.