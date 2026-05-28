import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    flips = 0
    operations = []

    for i in range(n-1, -1, -1):
        val = a[i]
        if flips & 1: val = -val

        if val > 0:
            gained = -sum([num for num in a[:i] if num<0])
            lost = sum([num for num in a[:i] if num>0])
            if gained>lost:
                flips += 1
                operations.append(i+1)

    print(flips)
    print(*operations)

t = int(input())
for _ in range(t): solve()
