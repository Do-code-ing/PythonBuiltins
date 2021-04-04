# 정수 값을 <0b>, <0o>, <0x>가 앞에 붙은 이진 문자열로 반환한다.
# 0b : 이진수 = bin(int) , binary number
# 0o : 8진수 = oct(int) , octal number
# 0x : 16진수 = hex(int) , hexadecimal

print(bin(10))
# 0b1010
print(oct(10))
# 0o12
print(hex(10))
# 0xa

# 0b, 0o, 0x를 제외하고 반환
print(f"{10:#b}")
# 0b1010
print(f"{10:b}")
# 1010
print(f"{10:o}")
# 12
print(f"{10:x}")
# a
print(f"{10:X}")
# A (대문자로)

# 참고
# c(character) 는 정수를 해당 유니코드 문자로 반환한다.
# print(f"{3575:c}")
# ෷