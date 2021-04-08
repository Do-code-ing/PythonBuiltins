# string.isalnum()
# 문자열의 문자가 모두 알파벳이나 숫자로 이루어졌다면 True, 아니라면 False를 반환한다.

a = "e12e1esa23F4G4"
print(a.isalnum())
# True

a = "e12e1es a23F4G4"
print(a.isalnum())
# False