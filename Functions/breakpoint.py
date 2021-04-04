# breakpoint(*args, **kws) (kws : keyword arguments)
# 함수 호출지점에서 디버거로 진입한다.
# sys.breakpointhook()를 호출하여 기본적으로 pdb.set_trace()를 호출하여, pdb(python debug) 디버거에 drop되지만,
# 다른 함수를 설정하여 사용할 디버거를 선택할 수 있다.

# breakpointhook을 인자로 감사 이벤트(auditing event)인 builtins.breakpoint를 발생시킨다.

breakpoint()