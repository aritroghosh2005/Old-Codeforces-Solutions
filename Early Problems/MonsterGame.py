from itertools import accumulate
from bisect import bisect_right, bisect_left
import sys

input = sys.stdin.readline

def findMaxScore(n, a, b):
    prev = -1
    maxScore = 0
    a.sort()
    bCumm = list(accumulate(b))
    for x in a:
        if x == prev: continue
        prev = x
        score = 0
        swords = n - bisect_left(a, x)
        levels = bisect_right(bCumm, swords)
        score = levels*x
        if score>=maxScore: maxScore = score
    return maxScore

t = int(input())
results = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    results.append(findMaxScore(n,a,b))

for r in results:
    print(r)



