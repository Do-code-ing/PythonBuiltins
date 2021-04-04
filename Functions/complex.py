# complex([real[,imag]]) : real number(실수), imaginary nember(허수)
# class이며, real + imag*1j 값을 가진 복소수를 돌려주거나, 문자열 또는 숫자를 복소수로 변환한다.
# 첫 번째 parameter가 문자열이면 복소수로 해석되며, 두번째 parameter없이 함수를 호출해야 한다.
# 두 번째 parameter는 결코 문자열 일 수 없다.
# 각 argument는 (복소수를 포함한)int 형이 될 수 있다.
# imag가 생략되면 기본값은 0이고, 생성자는 int와 float과 같은 숫자 변환으로 사용된다.
# 두 arguments가 모두 생략되면 0j를 돌려준다.

a = 123
b = 345

# real 만 넣었을 때
print(complex(a))
# (123+0j)

# 두 arguments를 다 넣었을 때
print(complex(a,b))
# (123+345j)

# 두 argumnets 모두 생략할 때
print(complex())
# 0j

# 참고
# 문자열을 변환할 때, 문자열은 중앙의 + 또는 - 연산자 주위에 공백을 포함해서는 안 된다.
# 예를 들어, complex('1+2j') 는 괜찮지만 complex('1 + 2j') 는 ValueError 를 일으킨다.