import sys
input = lambda : sys.stdin.readline().rstrip()

from math import ceil

def solve():
    n, m, k = map(int, input().split())
    s = n // k

    playerJokers = min(s, m)
    leftJokers = m - playerJokers

    opponentJokers = ceil(leftJokers / (k-1) )
    print(playerJokers - opponentJokers)

t = int(input())
for _ in range(t): solve()
