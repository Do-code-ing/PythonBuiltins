# with
# 컨텍스트 관리자가 정의한 method 내에서 코드 블록의 실행을 래핑하는데 사용된다.
# 컨텍스트 관리자란, try... except와 같이 __enter__... __exit__method를 구현하는 class다.
# (리소스 관리 및 예외 처리에 사용된다.)
# (예를 들어, 예외가 발생하면 파일 스트림 프로세스가 다른 르로세스를 차단하지 않고 제대로 종료되도록 한다.)

with open("test.txt", "w") as test:
    test.write("This is for a test.")

# test.txt가 생긴 것을 확인해보자
