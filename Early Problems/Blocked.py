import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if len(set(a)) == n:
        print(*sorted(a, reverse=True))
    else: print(-1)

t = int(input())
for _ in range(t):
    solve()