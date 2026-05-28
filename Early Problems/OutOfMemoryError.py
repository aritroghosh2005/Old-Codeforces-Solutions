import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n,m,h = map(int, input().split())
    a = list(map(int, input().split()))
    aOriginal = a[:]

    updates = [0]*n
    crashes = 0

    for i in range(m):
        b,c = map(int, input().split())
        idx = b - 1
        
        if updates[idx] < crashes:
            a[idx] = aOriginal[idx]
            updates[idx] = crashes  
        a[idx] += c

        if a[idx] > h: crashes += 1

    for i in range(n):
        if updates[i] < crashes: a[i] = aOriginal[i]
    print(*a)

t = int(input())
for _ in range(t):
    solve()