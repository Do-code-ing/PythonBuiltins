# list.sort(key=..., reverse=...)
# list를 정렬한다.
# key : 정렬 비교를 위한 key 역할을 하는 함수를 제공하면 된다.
# reverse : True가 제공되는 경우, 역순 또는 내림차순으로 정렬된다.

lst = [1,3,6,4,2]
lst.sort()
print(lst)
# [1, 2, 3, 4, 6]

# reverse
lst = ["z","i","a","d"]
lst.sort(reverse=True)
print(lst)
# ['z', 'i', 'd', 'a']

# key 길이순으로 정렬
lst = ["ab","abcdefg","abcd","abc"]
lst.sort(key=len)
print(lst)
# ['ab', 'abc', 'abcd', 'abcdefg']