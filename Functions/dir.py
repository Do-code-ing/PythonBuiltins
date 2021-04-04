# dir(object) : directory
# object의 directory를 반환한다.
# arguments가 없다면, 현재 파일 범위의 이름들을 알파벳 순서의 목록으로 반환한다.

# arguments가 없는 경우
print(dir())
# ['__annotations__', '__builtins__', ... ,'__spec__']

# module을 부른 후
import random

print(dir())
# ['__annotations__', '__builtins__', ... ,'__spec__', 'random']

# object가 moduel이라면 moduel 내부에서 __dir__로 선언된 것들도 반환한다.
print(dir(random))
# ['BPF', 'LOG4', ... , 'vonmisesvariate', 'weibullvariate']

# __dir__로 선언된 것이 없다면, 그 object와 object의__dict__ attribute를 반환하기 위해 시도한다.
# 결과로 나온 목록은 확실하지 않으며, getattr을 사용할 때 그 정보는 부정확할 수 있다.
# 왜냐하면 dir()의 mechanism은 다른 type들의 object에서는 다르게 동작하는데,
# 완전한 정보보다는 가장 적절한 정보를 만들려고 시도하기 때문이다.

# 참고
# dir() 은 주로 '대화형 prompt'에서의 사용 편의를 위해 제공되기 때문에,
# 엄격하거나 일관되게 정의된 이름들의 집합을 제공하기보다 흥미로운 이름들의 집합을 제공하려고 시도하며,
# 상세한 동작은 배포마다 변경될 수 있다. 예를 들어, arguments가 class면 metaclass attribute는 결과 리스트에 없다.