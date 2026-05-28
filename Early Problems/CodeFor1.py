from numba import njit

import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def length(n):
    if n<=1: return 1
    return 2*length(n//2)+1

def countOnes(n, start, end):
    if n<=1: return n

    left = length(n//2)
    mid = left
    right = left+1

    count = 0

    if start<left:
        leftEnd = min(end, left-1)
        count += countOnes(n//2, start, leftEnd)

    if start <= mid <= end: count += (n%2)

    if end>=right:
        rightStart = max(0, start - right)
        rightEnd = end - right
        count += countOnes(n//2, rightStart, rightEnd)

    return count

n, l, r = map(int, input().split())
print(countOnes(n, l-1, r-1))



