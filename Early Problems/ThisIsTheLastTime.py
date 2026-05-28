import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n, k = map(int, input().split())
    casinos = []
    for _ in range(n):
        l, r, real = map(int, input().split())
        casino = {"low":l, "high": r, "prize": real}
        casinos.append(casino)
    casinos.sort(key = lambda x: (x["low"], x["prize"]))

    coins = k    
    for casino in casinos:
        if casino["prize"] <= coins: continue
        if casino["low"] <= coins <= casino["high"]: coins = casino["prize"]
    print(coins)            


t = int(input())
for _ in range(t):
    solve()