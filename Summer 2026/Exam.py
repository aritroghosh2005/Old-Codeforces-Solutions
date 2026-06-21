import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    ordering = []

    if n <= 2: ordering = [1]
    elif n==4: ordering = [3,1,4,2]
    else:
        for i in range(1, n//2 + 1):
            first, second = i, n - i + 1
            ordering.extend([first, second])

        if n>=5:
            remainder = i + 1
            ordering.insert(1, remainder)
        if n%2 == 0: ordering.pop()

    print(len(ordering))
    print(*ordering)

t = 1
for _ in range(t): solve()