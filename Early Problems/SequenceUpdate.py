import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))

    diff = r - l + 1

    leftPool = sorted(a[:r])
    rightPool = sorted(a[l-1:])
    s = min(sum(leftPool[:diff]), sum(rightPool[:diff]))
    print(s)

t = int(input())
for _ in range(t): solve()