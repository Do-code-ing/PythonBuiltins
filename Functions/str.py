# str(object='')
# str(object=b'', encoding='utf-8', errors='strict')
# class이며, object가 가진 문자열을 반환한다.
# encoding : encoding 할 종류를 제공하면 된다.
#            제공되지 않는 경우, 기본값은 'UTF-8'이다.
# errors : UnicodeDecodeError 발생 시, 처리하는 방식을 제공하면 된다.
#          기본값은 'strict'로 더 궁금하다면, 아래의 주소에 들어가 보도록 하자.
#          https://www.programiz.com/python-programming/methods/built-in/str

# 문자열
str_a = str("Hello")
print(str_a)

# bytes
str_b = str(b"Hello")
print(str_b)

# encoding
bytes_a = bytes("안뇽췬구들", encoding="UTF-8")
str_c = str(bytes_a)
print(str_c)
# b'\xec\x95\x88\xeb\x87\xbd\xec\xb7\xac\xea\xb5\xac\xeb\x93\xa4'
str_d = str(bytes_a, encoding="UTF-8")
print(str_d)
# 안뇽췬구들