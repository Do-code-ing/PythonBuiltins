# memoryview(obj)
# class이며, argument로 부터 만들어진 'memoryview' object를 반환한다.
# obj는 bytes나 bytearray type이다.
# list나 str 등을 slicing 할 때 data를 복사하며 많은 자원을 사용하는데,
# 이러한 현상을 줄이기 위해 memoryview를 사용한다.

# memoryview object 만들기
bytes_a = bytes(123)
memoryview_a = memoryview(bytes_a)
print(memoryview_a)
# <memory at 0x000001D4D1A54E80>

str_a = "hello"
bytes_b = bytes(str_a, encoding="utf-8")
memoryview_b = memoryview(bytes_b)
print(memoryview_b)
# <memory at 0x000001D4D1BDC040>

bytearray_a = bytearray(range(3))
memoryview_c = memoryview(bytearray_a)
print(memoryview_c)
# <memory at 0x000001D4D1BDC100>

# slicing 하여 내용 수정하기
print(bytearray_a)
# bytearray(b'\x00\x01\x02')
memoryview_c[0] = 1
print(bytearray_a)
# bytearray(b'\x01\x01\x02')

# bytearray_a[0] = 1 은
# memoryview_c[0] = 1 과 같은 결과값을 갖지만,
# 후자의 경우 실제 처리과정에서 memoryview를 사용해서 처리했기 때문에,
# 대상을 복사하지않고 slicing 했기 때문에, 과정이 줄어들어 속도가 그 만큼 빠르다.
# 아래의 코드를 진행해보고 결과값이 어떻게 나오는지 참고하자.

import time

# data의 길이가 n만큼인 bytes를 바로 slicing 할 때
for n in (100000, 200000, 300000, 400000):
    data = 'x'.encode()*n
    start = time.time()
    b = data
    while b:
        b = b[1:]
    print("bytes", n, time.time()-start)

# data의 길이가 n만큼인 bytes의 memoryview로 slicing 할 때 
for n in (100000, 200000, 300000, 400000):
    data = 'x'.encode()*n
    start = time.time()
    b = memoryview(data)
    while b:
        b = b[1:]
    print("memoryview", n, time.time()-start)

# bytes 100000 0.13702964782714844
# bytes 200000 0.891430139541626
# bytes 300000 1.6393804550170898
# bytes 400000 2.471931219100952
# memoryview 100000 0.011998414993286133
# memoryview 200000 0.023884296417236328
# memoryview 300000 0.03711986541748047
# memoryview 400000 0.04699516296386719
# bytes에서와 memoryview에서 slicing 속도 차이는,
# data의 양이 100,000개 일 때는 약 10배,
# 400,000개 일 때 약 50배정도로 memoryview가 빠르다는 결과를 보여주는데,
# 더 많다면 그 속도 차이는 기하급수적으로 늘어날 것이다.