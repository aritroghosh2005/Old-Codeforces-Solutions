def maxLayers(a,b):
    a1, b1 = a,b
    layersW = layersD = 0
    k = 0
    # Case 1: White chocolate on top
    while True:
        if k%2 == 0: # Turn of white chocolate
            if a1>=2**k: a1 -= 2**k 
            else: break
        else: # Turn of dark chocolate
            if b1>=2**k: b1 -= 2**k 
            else: break
        k += 1
        layersW += 1
 
    k=0
    # Case 2: Dark chocolate on top
    while True:
        if k%2 == 1: # Turn of white chocolate
            if a>=2**k: a -= 2**k 
            else: break
        else: # Turn of dark chocolate
            if b>=2**k: b -= 2**k 
            else: break
        k += 1
        layersD += 1
        
    return max(layersW, layersD)
    
n = int(input())
kgs = []
for i in range(n):
    kgs.append(input().split())
    for j in range(2):
        kgs[i][j] = int(kgs[i][j])
 
print()
for i in range(n):
    print(maxLayers(kgs[i][0], kgs[i][1]))