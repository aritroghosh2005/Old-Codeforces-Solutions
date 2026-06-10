import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    bArray = list(map(int, input().split()))

    bArray.sort(reverse=True)

    for i in range(n-2):
        b1, b2, b3 = bArray[i], bArray[i+1], bArray[i+2]
        
        if b3==b1%b2: continue
        else: 
            print(-1)
            return

    print(bArray[0], bArray[1])


t = int(input())
for _ in range(t): solve()