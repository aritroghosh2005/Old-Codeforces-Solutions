import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n, q = map(int, input().split())
    a = ['$'] + list(map(int, input().split()))
    b = ['$'] + list(map(int, input().split()))

    a[n] = max(a[n], b[n])
    for i in range(n-1, 0, -1): a[i] = max(a[i], b[i], a[i+1])

    sums = [0]*(n+1)
    for i in range(1, n+1):
        sums[i] = sums[i-1] + a[i]

    results = []
    for _ in range(q):
        l,r = map(int, input().split())
        results.append(sums[r] - sums[l-1])
    print(*results)

t = int(input())
for _ in range(t): solve()