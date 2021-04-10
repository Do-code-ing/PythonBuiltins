# 멤버십 연산자 (Membership Operator)
# 값이 sequence의 구성원인지 여부를 테스트한다.
# in, not in 이 있다.

# 구성원이 맞는지 : in
pets = ["dog", "cat", "ferret"]
print("fox" in pets)
# False
print("cat" in pets)
# True
print("me" in "disappointment")
# True

# 구성원이 아닌지 : not in
print("pot" not in "disappointment")
# True