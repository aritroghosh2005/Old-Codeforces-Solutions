def findWinner(n, a, b):
    for i in range(n, 0, -1):
        if a[i-1] != b[i-1]: break

    Ascore = Mscore = 0
    for j in range(n):
        Ascore ^= a[j-1]
        Mscore ^= b[j-1]
    
    if Ascore != Mscore:
        if i%2==1: print("Ajisai")
        else: print("Mai")
    else:
        print("Tie")




N = int(input())
tests = []
for _ in range(N):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    tests.append([n,a,b])

for _ in range(N):
    findWinner(tests[_][0], tests[_][1], tests[_][2])

