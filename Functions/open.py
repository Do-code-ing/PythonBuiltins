# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# file을 열고 해당 file object를 반환한다.
# file을 열 수 없으면 'OSError'가 발생한다.
# file : 열 file의 경로명을 주는 'path-like object'를 입력하면 된다.
# mode : file이 열리는 mode를 지정하는 선택적 문자열을 입력하면 된다.
#        선택적 문자열에는 다음과 같은 종류가 있다.
#        'r' : 읽기 전용으로 연다.(기본값)
#        'w' : 쓰기 전용으로 열고, 파일을 먼저 자른다.
#        'x' : 독점적인 파일 만들기 전용으로 연다. 이미 존자하는 경우에는 실패한다.
#        'a' : 쓰기 전용으로 열고, 파일이 존재하는 경우에는 파일의 끝에 덧붙인다.
#        'b' : binary mode
#        't' : text mode (기본값)
#        '+' : 갱신(읽기 및 쓰기) 전용으로 연다.
# buffering : buffering 정책을 설정하는데 사용되는 선택적 정수를 입력하면 된다.
# encoding : file을 encoding하거나 decoding할 때 사용되는 encoding의 이름을 입력하면 된다.
#            text mode에서만 사용해야한다.
# error : encoding 및 decoding errors를 처리하는 방법을 지정하는 선택적 문자열을 입력하면 된다.
#         binary mode에서는 사용할 수 없다.
# newline : 'universal newlines' mode가 작동하는 방식을 제어한다.
#           제어 방식에는 None, '', '\n', '\r', '\r', '\n' 이 있다.
#           text mode에만 적용된다.
# closefd : True 외에 다른값이 주어진다면 예외처리가 발생한다.
#           기본값 = True
# opener : custom opener로 써, open file descriptor를 반환해야 한다.

# 조금 더 자세한 내용을 알고 싶다면 아래의 주소에 들어가 보도록 하자.
# https://docs.python.org/ko/3/library/functions.html#open
# https://www.programiz.com/python-programming/methods/built-in/open

# 참고
# file object와 관련된 함수를 알고 싶다면 아래의 주소에 들어가 보도록 하자.
# https://docs.python.org/ko/3/tutorial/inputoutput.html#tut-files

# file 열어보기

# 현재 목록에서 file 열기
f = open("text.txt")
# # 모든 경로를 지정해서 열기
f = open("c:/python39/readme.txt")

# mode 사용해서 열기

# 읽기 전용
f = open("path_to_file", mode="r")
# 쓰기 전용
f = open("path_to_file", mode="w")
# (이어)쓰기 전용
f = open("path_to_file", mode="a")

# python의 encoding 기본값은 ASCII다.
# 그래서 다음과 같이 encoding을 변경할 수 있다.
f = open("path_to_file", mode="r", encoding="utf-8")

# 사용 예제
# 출처 : 나도코딩 Youtube, tistory
# https://www.youtube.com/channel/UC7iAOLiALt2rtMVAWWl4pnw/videos
# https://nadocoding.tistory.com/category/%ED%8C%8C%EC%9D%B4%EC%8D%AC%20%EA%B0%95%EC%9D%98/%EA%B8%B0%EB%B3%B8%ED%8E%B8

score_file = open("score.txt", "w", encoding="utf8") #open을 통해 파일을 열고, 파일명, write, utf8방식으로 유니코드 인코딩
print("수학 : 0",file=score_file) #score_file에 내용 입력
print("영어 : 50",file=score_file)
score_file.close() # 연 파일을 닫다.

score_file = open("score.txt", "a", encoding="utf8") # a means append, 이어쓰기
score_file.write("과학 : 80") 
score_file.write("\n코딩 : 100") #write를 쓰면 줄바꿈이 안되기에 \n으로 줄바꿈
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r means read 읽다
print(score_file.read()) # 한번에 다 읽어오기
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(),end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True: # 참일 때까지 반복
    line = score_file.readline() # line 변수 지정
    print(line,end="") # line 출력
    if not line: # line이 없으면
        break # 멈춰라
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()