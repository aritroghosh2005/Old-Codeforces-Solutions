import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n,m = map(int, input().split())
    a = [-1] + list(map(int, input().split()))

    span = 1
    for i in range(2, n+1):
        if a[i] == a[i-1]: span += 1
        else: span = 1

        if span >= m: 
            print("NO")
            break
    else: print("YES")

t = int(input())
for _ in range(t):
    solve()