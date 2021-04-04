# sorted(iterable, *, key=None, reverse=False)
# iterable의 항목들을 정렬하여 새 sorted list로 반환한다.
# key : str.lower과 같은 elements를 비교하는 함수를 제공하면 된다.
#       (해당 함수의 비교법을 가져와서 쓴다.)
# reverse : True인 경우 반대로 정렬한다.
# 급여를 등급별로 나눠서 주기위해 부서별로, 직급별로, 등 여러번 정렬할 때 유용하다.

# 정렬해보자
lst = ["a", "b", "A", "B"]
sorted_a = sorted(lst)
print(sorted_a)
# ['A', 'B', 'a', 'b']

# str.lower
sorted_b = sorted(lst, key=str.lower)
print(sorted_b)
# ['a', 'A', 'b', 'B']

sorted_c = sorted(lst, key=str.islower)
print(sorted_c)
# ['A', 'B', 'a', 'b']

# 여러번 정렬
# 이름, 학점, 봉사점수를 가진 사람들을 만들고
students = [
    ("Sang-Min", "A", 25),
    ("Sang-Hyuck", "B", 20),
    ("Hyun-Ji", "C", 30)
]

# 학점이 높은 순으로
good_grade_sorted = sorted(students, key=lambda x:x[1])
print(good_grade_sorted)

# 봉사점수가 높은 순으로
good_volunteer_sorted = sorted(students, key=lambda x:x[2], reverse=True)
print(good_volunteer_sorted)