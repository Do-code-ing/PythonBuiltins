# globals()
# 현재 global symbol table을 나타내는 dictionary를 갱신하고 반환한다.
# 반환받은 dictionary는 항상 현재 module의 dictionary다.
# function 또는 method 내에서 사용하면, module이 어디서 호출되었는가가 아니라, 어디서 정의되었는지를 반환한다.

globals()
# # "c:/Users/pc/Desktop/..."
print(globals())
# {'__name__': '__main__', '__doc__': None, ', ... }

# locals()
# 현재 local symbol table을 나타내는 dictionary를 갱신하고 반환한다.
# function blocks에서 호출될 때는 자유 변수를 반환하지만, class blocks에서는 그렇지 않다.

locals()
# "c:/Users/pc/Desktop/..."
print(locals())
# {'__name__': '__main__', '__doc__': None, ', ... }

# 참고
# locals() 로 반환받은 dictionary 내용은 수정해서는 안된다.
# 수정했을 때 interpreter가 사용하는 지역 및 자유 변수의 값에 영향을 미치지 않을 수 있기 때문이다.