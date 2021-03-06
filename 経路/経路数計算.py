"""  ABC042 D

重複のある組み合わせ数の計算 (a+b)! / a!b! を利用した経路数探索問題

https://atcoder.jp/contests/abc042/tasks/arc058_b
"""

H, W, A, B = map(int, input().split())

#  H行W列 左下から縦A横B


#  mod 10**9 + 7 を求めるやつ
def mod(num):
    return num % (10 ** 9 + 7)

n = H + W + 1

fac = [0] * n  # 階乗
rev = [0] * n  # 逆元

fac[0] = 1

for i in range(1, n):
    fac[i] = mod(fac[i-1] * i)


#  逆元の計算 x**(-1) ≡ x**(10**9 + 5) (mod 10**9 + 7)
rev[n-1] = pow(fac[n-1], 10**9 + 5, 10**9 + 7)

#  ((M-1)!)**-1 * (M-1) -> ((M-2)!)**-1 を利用
for i in range(n - 2, 0, -1):
    rev[i] = mod(rev[i + 1] * (i + 1))

rev[0] = 1

res = 0

for i in range(W - B):
    #  r:(H-A-1, i+B)までの経路数 rr:(H-A, i+B)からの経路数
    r = mod(fac[H - A - 1 + i + B] * mod(rev[B + i] * rev[H - A - 1]))
    rr = r * mod(fac[A - 1 + W - B - 1 - i] * mod(rev[A - 1] * rev[W - B - 1 - i]))
    res = mod(res + rr)
    
print(res)
