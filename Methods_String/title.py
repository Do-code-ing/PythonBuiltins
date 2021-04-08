# str.title()
# 문자열에서 단어의 첫 글자는 대문자, 나머지 문자는 소문자로 변환 후 반환한다.

str_a = "hello world"
print(str_a.title())
# Hello World

# a-zA-z를 제외한 것을 기준으로 split하여 단어라고 정의하기 때문에
# they're 같은 경우에는 They'Re로 나올 수 있음을 주의

# 정규식을 통해 해결할 수 있음
# >>> import re
# >>> def titlecase(s):
# ...     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
# ...                   lambda mo: mo.group(0).capitalize(),
# ...                   s)
# ...
# >>> titlecase("they're bill's friends.")
# "They're Bill's Friends."