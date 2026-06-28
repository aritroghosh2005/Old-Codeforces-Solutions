import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n, k = map(int, input().split())
    valLeft = n
    popCount = 0

    for exp in range(100):
        val = 2**exp
        freq = min(k, valLeft//val)

        valLeft -= val*freq
        popCount += freq
        if valLeft <= 0: break
    print(popCount)

t = int(input())
for _ in range(t): solve()