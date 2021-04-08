# string.isidentifier() (identifier : 식별자)
# 문자열이 식별 유효한 식별자면 True, 아니라면 False를 반환한다.
# Python 식별자는 변수, 함수, 클래스, 모듈 또는 기타 객체를 식별하는 데 사용되는 이름이다.
# 즉 변수명으로 사용할 수 있다면 isidentifier의 결과는 True다.

a = ""
print(a.isidentifier())
# False

a = "hello"
print(a.isidentifier())
# True

a = "hello 33"
print(a.isidentifier())
# False

a = "33hello"
print(a.isidentifier())
# False