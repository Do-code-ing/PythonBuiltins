# filter(function, iterable)
# function이 True를 돌려주는 iterable elements로 iterator를 구축한 filter object를 반환한다.

num_list = [0,1,2,3,4]

# 함수를 사용하지 않고 filter object 만들기
filter_a = filter(None, num_list)
print(filter_a)
# <filter object at 0x000002022D589FA0>

# 출력하기 위해 list object로 만들어 보자.
list_a = list(filter_a)
print(list_a)
# [1, 2, 3, 4]
# 결과값 0은 iterable하지 않으므로 반환하지 않는다.

# lambda 함수를 사용
list_b = list(filter(lambda x:x-1,num_list))
print(list_b)
# [0, 2, 3, 4]
# 0 - 1 = -1 이므로 0은 반환된다.
# 1 - 1 = 0 이므로 1은 반환되지 않는다.

list_c = list(filter(lambda x:x%2==0,num_list))
print(list_c)
# [0, 2, 4]

# 참고
# lambda
# lambda x1:x2, x3 (x1 = x2 = x3, 직관성을 위해 숫자 기입)
# x2의 elements를 x1 위치에 차례로 대입시켜 x2의 형태로 만든다.