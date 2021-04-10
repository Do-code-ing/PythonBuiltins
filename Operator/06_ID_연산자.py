# ID 연산자 (Identity Operator)
# 두 피연산자가 ID를 공유하는지 테스트한다.
# is, is not 이 있다.

# ID가 같은지 : is
print(id(2) is id(20))
# False
a = "2"
b = '2'
print(a is b)
# True

# ID가 다른지 : is not
print(a is not b)
# False

# 참고
# Python 3.8 부터,
# 다음과 같이 문자열이나 숫자를 is를 통해 비교할 경우 'SyntaxWarning'이 발생한다.
# print(2 is 2)
# True
# SyntaxWarning: "is" with a literal. Did you mean "=="?