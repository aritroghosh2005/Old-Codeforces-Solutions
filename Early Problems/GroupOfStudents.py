from itertools import accumulate
from bisect import bisect_right, bisect_left

m = int(input())
c = list(map(int, input().split()))
x,y = map(int, input().split())

cTot = list(accumulate(c))

start = bisect_left(cTot, x)
end = bisect_right(cTot, y)

for i in range(start, end+1):
    beginners = sum(c[:i+1])
    intermediates = sum(c[i+1:])
    if x <= beginners <=y and x <= intermediates <= y:
        print(i+2)
        break
else:
    print(0)


