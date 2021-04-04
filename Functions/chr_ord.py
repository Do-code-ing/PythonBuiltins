# chr(i) : character(int)
# 유니코드 포인트 정수 값을 입력하면 해당 정수 값의 유니코드 문자열을 반환한다.
# i 가 0 ~ 1,114,111(16진수로 0x10FFFF)를 벗어나면 'ValueError'가 발생한다.

# 정수를 문자로
print(chr(8364))
# '€'

# ord(c) : ordinary character(character)
# 유니코드 문자열이 주어지면 해당 문자의 유니코드 코드 포인트 정수 값을 반환한다.
# chr() 와 반대로 작동한다.

# 문자를 정수로
print(ord("€"))
# 8364