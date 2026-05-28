import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

from functools import cache

@cache
def fibo(n):
    if n<=1: return n
    return fibo(n-1) + fibo(n-2)

num = int(input())
if num==0: exit("0 0 0")
elif num==1: exit("0 0 1")

i=0
while True:
    if fibo(i)==num: break
    i+=1
print(fibo(i-4), fibo(i-3), fibo(i-1))
    

