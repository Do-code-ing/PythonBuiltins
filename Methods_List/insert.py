# list.insert(i, elem)
# list에 elem을 i index에 삽입한다.
# 원래 index의 뒷 순서부터 한 차례씩 밀린다.

lst = [1,2,3,4,5]
lst.insert(2, 6)
print(lst)
# [1, 2, 6, 3, 4, 5]