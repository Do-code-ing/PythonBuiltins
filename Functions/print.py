# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# objects를 출력한다.
# sep : separate, object사이에 구분될 내용을 제공하면 된다.
#       기본값 = ' '
# end : 내용을 출력한 뒤 끝에 올 내용을 제공하면 된다.
#       기본값 = '\n'
# file : write(string) method가 있는 object여야한다.
#        기본값 = sys.stdout(화면에 objects를 출력하는 sys 함수)
# flush : 출력의 buffering 여부를 만든다. True인 경우, stream이 강제로 flush된다. (line 34)
#         기본값 = False

# objects만 사용
import time

name = "Sang-Min"
str_a = "안녕?"
print(name, "이(가) 말합니다.", str_a)
# Sang-Min 이(가) 말합니다. 안녕?

# sep 사용
print(name, "이(가) 말합니다.", str_a, sep=" (띄고) ")
# Sang-Min (띄고) 이(가) 말합니다. (띄고) 안녕?

# end 사용
print(name, "이(가) 말합니다.", str_a, end=" (이)라고 말이죠.\n")
# Sang-Min 이(가) 말합니다. 안녕? (이)라고 말이죠.

# file 사용 (기존 print_file.txt를 삭제해보고 진행해보자)
p_file = open("./print_file.txt", "w", encoding="utf-8")
print(name, "이(가) 말합니다.", str_a, file=p_file)
# 새로 생긴 'print_file.txt'를 확인해보세요.

# flush 사용
for i in range(1, 6):
    print(i, end=" ", flush=True)
    time.sleep(1)

print(" ")
for i in range(1, 6):
    print(i, end=" ")
    time.sleep(1)
# 직접 실행해보고 어떤 결과가 나오는지 확인해보자.
