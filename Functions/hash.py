# hash(object)
# hash 값이 있다면(object가 hashable 하다면), object의 hash 값을 반환한다.
# hash 값은 정수다.
# dictionary 조회 중에 dictinary의 key를 빠르게 비교하는데 사용된다.
# 같다고 비교되는 숫자 값은 같은 hash 값을 갖는다.
# 예를 들어, 1과 1.0은 int와 float이지만 같은 hash 값을 갖는다.

# hash 값 만들기
tuple_a = "name", "age", "country", "1", "1.0"
hash_value_a = hash(tuple_a)
print(hash_value_a)
# tuple_a에 대한 hash 값 

list_b = ["name", "age", "country"]
hash_value_b_0 = hash(list_b[0])
print(hash_value_b_0)
# list_b의 0 번째 index 값의 hash 값

# dictionary의 경우
# dic_a = {"name":"Sang-Min", "age":27, "country":"Korea"}
# hash(dic_a)
# TypeError: unhashable type: 'dict'
# hashable 하지 않아서 안됨

# 참고
# hashable한 type에는 불변형인 type만 가능하다
# 불변형에는 bool, int, float, tuple, str, frozenset이 있다.