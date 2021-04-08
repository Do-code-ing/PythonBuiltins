# frozenset([iterable])
# set([iterable])
# 둘 다 class이며, iterable elements를 각각 frozenset object, set object로 반환한다.
# set은 가변형이며, add() 나 remove() 와 같은 method를 통해 내용을 변경할 수 있다.
# 가변형이기 때문에 hash value가 없으며 dictionary key 또는 다른 set의 element로 사용할 수 없다.
# frozenset은 불변형이며, elements는 hashable하다.
# 따라서 dictionary key 또는 다른 set의 element로 사용할 수 있다.
# 예를 들어, hash = {frozenset : value} 가 가능하다.

set_a = {1,2,3}
set_b = {4,5,6}
set_c = {1,2,3,4,5}
set_d = {1,2,4,5,6}

# set과 frozenset 만들기
frozenset_b = frozenset(set_b)
print(set_a)
# {1, 2, 3, 4, 5, 6}
print(frozenset_b)
# frozenset({7, 8, 9, 10, 11, 12})

### set과 frozenset 모두 사용 가능한 연산 ###

# set의 길이
print(len(set_a))
# 6

# set_a 에 해당 element가 있는지 검사
print((1 in set_a))
# True
print((7 in set_a))
# False

# set_a 에 해당 element가 없는지 검사
print(2 not in set_a)
# False
print(10 not in set_a)
# True

# 두 집합이 서로소인지 검사
print(set_a.isdisjoint(set_b))
# True
print(set_a.isdisjoint(set_c))
# False

# 해당 집합이 받아온 집합의 부분집합인지 검사
print(set_a.issubset(set_c))
print(set_a <= set_c)
# True
# 진부분집합인지 검사
print(set_a < (set_c))
# True

# 받아온 집합이 해당 집합의 부분집합인지 검사
print(set_c.issuperset(set_a))
print(set_c >= (set_a))
# True
# 진상위집합인지 검사
print(set_c > (set_a))
# True

# 두 집합의 합집합 반환
print(set_a.union(set_b))
print(set_a | set_b)
# {1, 2, 3, 4, 5, 6}

# 두 집합의 교집합 반환
print(set_a.intersection(set_c))
print(set_a & set_c)
# {1, 2, 3}

# 해당 집합에는 있으나 받아온 집합에는 없는 차집합 반환
print(set_c.difference(set_a))
print(set_c - set_a)
# {4, 5}

# 두 집합의 대칭차집합 반환
print(set_b.symmetric_difference(set_d))
print(set_b ^ set_d)
# {1, 2}

# 집합의 복사본 반환
# variable = set 을 사용해 복사하면, 기존 set의 내용이 바뀌게 될 경우 복사본 또한 내용이 바뀌게 된다.
print(set_a)
set_e = set_a
print(set_e)
set_a.add(8)
print(set_e)
# variable = set.copy() 를 사용해 복사하면, 기존 set의 내용을 바꿔도 복사본은 바뀌지 않는다.
print(set_b)
set_f = set_b.copy()
print(set_f)
set_b.add(9)
print(set_f)

# 참고
# union(), intersection() ... method들은 임의의 iterable을 argument로 받는데,
# operator(연산자)는 arguments가 sets 인 것을 필요로 한다.
# 그렇기에 |, & ... method들을 사용할 경우 오류가 발생할 수 있어서
# 읽기 쉬운 전자의 method를 사용할 것을 권장한다.

### set 에서만 사용할 수 있는 연산 ###

set_a = {1,2,3}
set_b = {4,5,6}
set_c = {1,2,3,4,5}
set_d = {1,2,4,5,6}

# 두 집합의 합집합을 해당 집합에 반환
set_a.update(set_b)
set_a |= set_b
print(set_a)
# set_a = {1, 2, 3, 4, 5, 6}

# 두 집합의 교집합을 해당 집합에 반환
set_b.intersection_update(set_c)
set_b &= set_c
print(set_b)
# set_b = {4, 5}

# 두 집합의 차집합을 해당 집합에 반환
set_a.difference_update(set_b)
set_a -= set_b
print(set_a)
# set_a = {1, 2, 3, 6}

# 두 집합의 대칭차집합을 해당 집합에 반환
set_a.symmetric_difference(set_d)
set_a ^= set_d
print(set_a)
# set_a = {3, 4, 5}

# 집합에 element를 추가 후 반환
set_a.add(1)
print(set_a)
# {3, 4, 5, 1}

# 집합에서 element를 제거 후 반환, element가 집합에 없다면 KeyError 발생
set_a.remove(5)
print(set_a)
# {3, 4, 1}

# 집합에 element가 있다면 제거 후 반환, Error 발생하지 않음
set_a.discard(2)
set_a.discard(3)
print(set_a)
# {4, 1}

# 집합에서 임의의 element를 제거 후 반환
set_g = {"1","2","3","4","5","6"}
set_g.pop()
print(set_g)
# 참고
# 집합이 모두 숫자라면 맨 앞의 element 제거
set_h = {1,2,3,4,5}
set_h.pop()
print(set_h)
# {2, 3, 4, 5}

# 집합을 공집합으로 만들고 반환
set_h.clear()
print(set_h)
# set()