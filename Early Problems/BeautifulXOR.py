def findOperations(a,b):
    if a==b: print(0)
    elif a^b < a:
        print(1)
        print(a^b)
    elif a^b > a:
        print(2)
        print(a,b)
    else: print(-1)

t = int(input())
tests = []
for _ in range(t):
    a,b = map(int, input().split())
    tests.append([a,b])
for _ in range(t):
    findOperations(tests[_][0], tests[_][1])