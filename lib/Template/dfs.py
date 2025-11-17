#  有向グラフ G = {0:[], 1:[]}

#  道の有無
def main():
    #  input()

    seen = [False] * N
    def dfs(num):
        seen[num] = True

        for nextnum in G[num]:
            if not seen[nextnum]:
                dfs(nextnum)

    #  s = 始点, t = 終点
    dfs(s)

    if seen[t]:
        print("Yes")
    else:
        print("No")

