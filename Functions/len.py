# len(s) : length(sequence)
# object의 길이나 항목의 갯수를 반환한다.
# argument는 sequence(str, bytes, tuple, list, range 등)이나
#            collection(dictionary, set, frozenset 등)일 수 있다.

# list인 경우
lst_a = ["kim", "lee", "park"]
print(len(lst_a))
# 3

# set인 경우
set_a = {"kim", "lee", "park"}
print(len(set_a))
# 3

# 참고
# CPython에서는
# 32비트 : 2**31 - 1
# 64비트 : 2**63 - 1
# 보다 긴 길이에서는 'OverflowError'가 발생한다.