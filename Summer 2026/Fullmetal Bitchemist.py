import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    s = input()

    total = n*(n+1) // 2
    freq = [0]*3
    freq[0] = 1

    runningSum = 0
    for ch in s:
        val = 1 if ch=='0' else 2
        runningSum = (runningSum+val)%3
        freq[runningSum] += 1
    
    sumZeroSubstrings = 0
    for count in freq:
        sumZeroSubstrings += count*(count-1) // 2

    hiddenSubstrings = 0
    length = 1
    
    for i in range(1, n):
        if s[i] != s[i-1]:
            length += 1
        else:
            if length >= 3:
                m = (length - 1) // 2
                hiddenSubstrings += m * (length - m - 1)
            
            length = 1
            
    if length >= 3:
        m = (length - 1) // 2
        hiddenSubstrings += m * (length - m - 1)

    ans = total - sumZeroSubstrings - hiddenSubstrings
    print(ans)

t = int(input())
for _ in range(t): solve()
