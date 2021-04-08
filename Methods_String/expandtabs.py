# string.expandtabs(tabsize)
# 문자열에 \t 기호가 있는 경우, tabsize만큼 조정하여 반환한다.
# tabsize의 기본값은 8이다.

a = "Hello\tWorld\tWellcome."
print(a.expandtabs())
# Hello   World   Wellcome.
print(a.expandtabs(10))
# Hello     World     Wellcome.