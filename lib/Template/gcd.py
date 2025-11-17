#  ユークリッドの互除法 未拡張

def gcd(x, y):
    if x < y:
        t = x
        x = y
        y = t

    if y == 0:
        return x

    else:
        return gcd(y, x % y)