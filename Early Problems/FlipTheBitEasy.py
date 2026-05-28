import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n, k = map(int, input().split())
    a = ['$'] + list(map(int, input().split()))
    p = int(input())

    val = a[p]
    valNot = 1 if val==0 else 0
    op = 0

    if valNot in a:
        start = a.index(valNot) 
        end = n - a[::-1].index(valNot)

        count1 = len([a[i] for i in range(start, p) if a[i+1] != a[i]]) if start < p else 0
        count2 = len([a[i] for i in range(p+1, end+1) if a[i-1] != a[i]]) if end > p else 0
        op = max(count1, count2) + 1
    else: op = 0
    print(op)

t = int(input())
for _ in range(t): solve()