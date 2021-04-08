# from, import
# import는 module을 불러올 때 사용한다.
import math
print(math.sqrt(16))
# 4.0

# from은 from... import로 사용되며, module에서 특정 함수를 불러올 때 사용한다.
# 이 방법으로 불러오면 math.sqrt()가 아닌, sqrt() 자체로 사용할 수 있다.
from math import sqrt
print(sqrt(16))
# 4.0