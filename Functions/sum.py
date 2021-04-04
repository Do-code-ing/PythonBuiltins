# sum(iterable, /, start=0)
# start 및 iterable의 항목들을 왼쪽에서 오른쪽으로 합하고 합계를 반환한다.
# iterable의 항목은 일반적으로 숫자며 시작 값은 문자열이 될 수 없다.
# (문자열 sequence를 합하고 싶다면, ''.join(sequence) 를 호출해보자.)
# start : 합할 때 제일 왼쪽에 둘 숫자를 제공하면 된다.


# 사용해보자
items_a = (n for n in range(101))
sum_a = sum(items_a)
print(sum_a)
# 5050

# start
items_b = (n for n in range(101))
sum_b = sum(items_b, 100)
print(sum_b)
# 5150