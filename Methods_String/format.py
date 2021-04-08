# template.format(p0, p1, ..., k0=v0, k1=v1, ...)
# 아래의 주소에 들어가 보도록 하자.
# https://www.programiz.com/python-programming/methods/string/format

# str.format(*args, **kwargs)
str_a = "{}, please {}.".format("Hey", "shut up")
print(str_a)
str_b = "Hello {}, your balance is {:9.3f}".format("Adam", 230.2346)
print(str_b)
# 9는 .을 포함한 숫자의 최대 길이
# .3f는 소수부분을 3자리까지 반올림하는 것을 의미 2346 -> 235

str_b = "Hello {}, your balance is {:9.3f}".format("Adam", 230.2346)
print(str_b)

import datetime

date = datetime.datetime.now()
print("It's now: {:%Y/%m/%d %H:%M:%S}".format(date))
print(f"It's now: {date:%Y/%m/%d %H:%M:%S}")

# complex number formatting
complexNumber = 1+2j
print("Real part: {0.real} and Imaginary part: {0.imag}".format(complexNumber))

# custom __format__() method
class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'

print("Adam's age is: {:age}".format(Person()))
