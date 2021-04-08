# is
# object의 id를 테스트하기 위해 사용된다.
# == 연산자는 두 variables가 같은지 여부를 테스트하는데 사용되지만,
# is 는 두 variables가 동일한 object를 참조하는지 테스트하는데 사용된다. 

print(True is True)
print(False is False)
print(None is None)
# True
# True, False, None은 instance가 각각 하나라서 동일하다고 판단한다.

print([] == [])
# True
print([] is [])
# False
print({} == {})
# True
print({} is {})
# False
# 가변형 object의 경우 각각 따로 존재하기 때문에 id가 다르다.

print("" == "")
print("" is "")
print(() == ())
print(() is ())
# True
# 불변형 object의 경우 동일한 메모리 위치를 참조한다.