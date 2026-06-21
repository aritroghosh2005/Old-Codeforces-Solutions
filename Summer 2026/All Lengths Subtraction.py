import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    p = list(map(int, input().split()))

    start = end = p.index(n)
    for i in range(n-1, 0, -1):
        if start > 0 and p[start-1] == i: start -= 1
        elif end < n-1 and p[end+1] == i: end += 1
        else: print("NO"); return
    print("YES")



t = int(input())
for _ in range(t): solve()
