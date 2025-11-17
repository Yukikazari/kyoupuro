""" ABC043 D

適当に切り取った文字列の過半数が同じ文字ならばアンバランス
aba や aa など2, 3文字内で偏りが無ければ全体でも発生し得ない

https://atcoder.jp/contests/abc043/tasks/arc059_b
"""

s = input()

if len(s) != 2:
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i] == s[i + 2]:
            print(i + 1, i + 3)
            exit()

else:
    if s[0] == s[1]:
        print(1, 2)
        exit()


print(-1, -1)