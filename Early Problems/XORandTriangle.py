import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    x = int(input())

    low = x & (-x)
    high = (~x) & (x+1)
    y = low | high

    print(y if y<x else -1)

t = int(input())
for _ in range(t):
    solve()