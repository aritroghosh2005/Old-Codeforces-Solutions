# This problem can be solved by greedy algorithm too
import sys
input = lambda : sys.stdin.readline().rstrip()
INF = 10**9 + 7

n = int(input())
op = 0

while n>0:
    d = max(map(int, str(n)))
    n -= d
    op += 1
print(op)
