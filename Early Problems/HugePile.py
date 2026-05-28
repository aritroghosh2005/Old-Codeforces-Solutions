from functools import cache
import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

@cache
def findTime(n, k, time=0):
    if n==k: return time
    if n<2*k-1: return -1

    option1 = findTime(n//2, k, time+1)
    option2 = findTime((n+1)//2, k, time+1)

    if option1==-1: return option2
    if option2==-1: return option1
    return min(option1, option2)


t = int(input())
times = []
for _ in range(t):
    n, k = map(int, input().split())
    times.append(findTime(n, k))

for _ in times:
    print(_)

