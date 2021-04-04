# bytearray([source[,encoding[,errors]]])
# class이며, 0 <= x < 256 범위에 있는 정수의 가변 sequence(순서, 차례를 배열하는)
# 정수 및 문자열을 새로운 '바이트 배열'로 반환한다.

# 정수인 경우
print(bytearray(0))
# bytearray(b'')
print(bytearray(1))
# bytearray(b'\x00')
print(bytearray(2))
# bytearray(b'\x00\x00')

# tuple, range, generator인 경우
print(bytearray((1,2)))
# bytearray(b'\x01\x02')
print(bytearray(range(5)))
# bytearray(b'\x00\x01\x02\x03\x04')
print(bytearray(i for i in range(0,6)))
# bytearray(b'\x00\x01\x02\x03\x04\x05')

# 문자열인 경우, (encoding 값을 넣는 경우)
print(bytearray("a", encoding="ASCII")) # ASCII로 인코딩하면 ASCII character의 range(128)안에 있어야 한다.
# bytearray(b'a')
print(bytearray("뛟꿻쮑", encoding="UTF-8"))
# bytearray(b'\xeb\x9b\x9f\xea\xbf\xbb\xec\xae\x91')
print(bytearray("뛟꿻쮑", encoding="UTF=8", errors=""))
# bytearray(b'\xeb\x9b\x9f\xea\xbf\xbb\xec\xae\x91'


# bytes([source[,encoding[,error]]])
# class이며, 0 <= x < 256 범위에 있는 정수의 불변 sequence
# 정수 및 문자열을 새로운 '바이트열' 객체로 반환한다.
# bytearray()와 같이 해석

# 정수인 경우
print(bytes(0))
# b''
print(bytes(1))
# b'\x00'
print(bytes(2))
# b'\x00\x00'
print(bytes(3))
# b'\x00\x00\x00'

# tuple, range, generator인 경우
print(bytes((1,2,3)))
# b'\x01\x02\x03'
print(bytes(range(20)))
# b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13'
print(bytes(i for i in range(0,5)))
# b'\x00\x01\x02\x03\x04'

# 문자열인 경우, (encoding 값을 넣는 경우)
print(bytes("a", encoding="ASCII")) # ASCII로 인코딩하면 ASCII character의 range(128)안에 있어야 한다.
# b'a'
print(bytes("뛟꿻쮑", encoding="UTF=8"))
# b'\xeb\x9b\x9f\xea\xbf\xbb\xec\xae\x91'
print(bytes("뛟꿻쮑", encoding="UTF=8", errors=""))
# b'\xeb\x9b\x9f\xea\xbf\xbb\xec\xae\x91'