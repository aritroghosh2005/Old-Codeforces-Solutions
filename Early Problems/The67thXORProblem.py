import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    maxXOR = 0

    for i in range(0, n):
        for j in range(i+1, n):
            xor = a[i]^a[j]
            if xor > maxXOR: maxXOR = xor
    print(maxXOR)

t = int(input())
for _ in range(t):
    solve()