# dict(**kwarg) : dictionary
# dict(mapping, **kwarg) (mapping objects : values에 key나 index가 있는 objects)
# dict(iterable, **kwarg)
# class이며, 새 dictionary를 만든다.
# dictionary의 기본형은 {key:value, key:value ...} 이다.

# dict()로 해당 variable을 dictionary로 만들 수 있다.
# 예를 들어, x = dict() 은 x = {} 와 대체로 같다. x = {} 의 경우 입력받는 값의 형태에 따라 set이 될 수 있다.
# dict(key=value, key=value ...)의 형식으로 값을 넣어 새 dictionary를 만들 수 있다.
# {key:value, key:value ...} 와 같다.

# dictionary 생성
a = dict(name = "Sang-Min", age = "27", country = "Korea")
print(a)
# {'name': 'Sang-Min', 'age': '27', 'country': 'Korea'}

# 빈 dictionary에 keys와 values 추가
b = {}
# b = dict()
# print(type(b))
# dictonary object[key] = value 의 형식으로 key와 value를 설정할 수 있다.
b[0] = "hello"
b[1] = "my"
b[2] = "dear"
print(b)
# {0: 'hello', 1: 'my', 2: 'dear'}

# enumerate()를 통해 iterable 객체를 index와 value로 나누어 각각 key와 value로 dictionary에 입력할 수 있다.
c = "hello", "my", "name", "is", "Sang-Min", "Lee"
d = {}
for idx, value in enumerate(c):
    d[idx] = value
print(d)
# {0: 'hello', 1: 'my', 2: 'name', 3: 'is', 4: 'Sang-Min', 5: 'Lee'}