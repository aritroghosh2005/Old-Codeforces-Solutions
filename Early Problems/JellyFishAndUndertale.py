import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

t = int(input())

for _ in range(t):
    a,b,n = map(int, input().split())
    tools = list(map(int, input().split()))

    time = b
    for x in tools:
        time += min(x, a-1)

    print(time)