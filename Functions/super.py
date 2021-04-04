# super([type[, object-or-type]])
# method 호출을 type의 부모나 형제 class에 위임하는 proxy object를 반환한다.
# class에서 재정의된 상속된 method를 access할 때 유용하다.
# object-or-type : 검색할 '메서드 결정 순서(method resolution order)'를 결정한다.
# base class의 이름을 명시 적으로 사용하지 않도록할 떄와,
# 다중 상속 작업을 할 때 유용하다.

# 사용해보자
# 출처 https://www.programiz.com/python-programming/methods/built-in/super
# 포유류
class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')

# 포유류인 개
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    # super() 를 사용해 상속받기
    super().__init__('Dog')
    
d1 = Dog()
# Dog has four legs.
# Dog is a warm-blooded animal.

# 다중 상속
# 동물
class Animal:
  def __init__(self, Animal):
    print(Animal, 'is an animal.');

# 동물 중에 포유류
class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
# 포유류 중에 날지 못하는 포유류
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammal):
    print(NonWingedMammal, "can't fly.")
    super().__init__(NonWingedMammal)

# 포유류 중에 수영 못하는 포유류
class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammal):
    print(NonMarineMammal, "can't swim.")
    super().__init__(NonMarineMammal)

# 수영도 못하고 날지도 못하는 포유류 중에 개
class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('Dog')
    
d = Dog()
print('')
bat = NonMarineMammal('Bat')
# Dog has 4 legs.
# Dog can't swim.
# Dog can't fly.
# Dog is a warm-blooded animal.
# Dog is an animal.

# Bat can't swim.
# Bat is a warm-blooded animal.
# Bat is an animal.

# 상속받는 순서
print(Dog.__mro__)
# (<class '__main__.Dog'>,
#  <class '__main__.NonMarineMammal'>,
#  <class '__main__.NonWingedMammal'>,
#  <class '__main__.Mammal'>,
#  <class '__main__.Animal'>,
#  <class 'object'>)

# base class인 'object'가 제일 마지막에 호출된다.
# super() 를 사용하여 협력적인 class를 설계하는 방법이 궁금하다면,
# 아래의 주소에 들어가 보도록 하자.
# https://rhettinger.wordpress.com/2011/05/26/super-considered-super/