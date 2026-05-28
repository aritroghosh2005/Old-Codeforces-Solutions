def findPair(n, a):
    x = y = 0
    for i in range(n):
        for j in range(i+1,n):
            x,y = a[i],a[j]
            if (y%x)%2==0:
                print(x,y)
                break
        else: continue
        break
    else:
        print(-1) 

    return -1

t = int(input())
tests = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    tests.append([n,a])

for _ in range(t):
    findPair(tests[_][0], tests[_][1])
