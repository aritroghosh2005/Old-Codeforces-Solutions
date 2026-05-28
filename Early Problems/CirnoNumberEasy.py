import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    a, n = map(int, input().split())
    d = list(map(int, input().split()))
    d.sort()

    a = str(a)
    dSmall, dBig = d[0], d[1]
    length = len(a)
    candidates = []

    if length>=2:
        number = int(str(dBig)*(length-1))
        candidates.append(number)
    
    if dSmall==0: number = int(str(dBig) + str(dSmall)*length)
    else: number = int(str(dSmall)*(length+1))
    candidates.append(number)

    number = 0
    for digit in a:
        digit = int(digit)
        closestDigit = min(d, key=lambda x: abs(digit-x))
        number = number*10 + closestDigit
    candidates.append(number)

    minDiff = float('inf')
    a = int(a)
    for candidate in candidates:
        diff = abs(candidate-a)
        minDiff = min(diff, minDiff)
    print(minDiff)

t = int(input())
for _ in range(t): solve()