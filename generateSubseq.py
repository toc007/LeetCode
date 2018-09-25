import time

def generateSubseq(A):
    if len(A) == 1:
        return [[A[0], A[0]]]
    
    subseq = generateSubseq(A[1:])
    subseqAdded = [[b for b in a] for a in subseq]
    for a in subseqAdded:
#        a[0] = max(A[0], a[0])
#        a[1] = min(A[0], a[1])
        if A[0] > a[0]:
            a[0] = A[0]
        elif A[0] < a[1]:
            a[1] = A[0]

    subseqAdded.append([A[0], A[0]])
    subseq.extend(subseqAdded)
    return subseq

def generateSubseqDC(A):
    if len(A) == 1:
        return [[A[0], A[0]]]
    elif len(A) == 0:
        return

    middle = len(A)/2
    left = generateSubseqDC(A[:middle])
    right = generateSubseqDC(A[middle:])

    #print "left: ", left
    #print "right: ", right

    res = left + right
    
    for l in left:
        for r in right:
            maxE = max(l[0], r[0])
            minE = min(l[1], r[1])
            res.append([maxE, minE])

    return res

def sumSubseqWidths(A, subseqGenerator):
    """
    :type A: List[int]
    :rtype: int
    """
    return reduce((lambda x, y: x + (max(y)-min(y))), subseqGenerator(A), 0)

#A = [21,12,8,21,11,35,36,10,30,29,28,1,24,23,36,30,38,17,14,37]
#print sumSubseqWidths(A, generateSubseqDC)
#print sumSubseqWidths(A, generateSubseq)

DCAvgTime = 0
for i in range(100):
    start = time.time()
    generateSubseqDC([21,12,8,21,11,35,36,10,30,29,28,1,24,23,36,30,38,17,14,37])
    DCAvgTime += time.time() - start
print DCAvgTime/100.

subseqAvgTime = 0
for i in range(100):
    start = time.time()
    generateSubseq([21,12,8,21,11,35,36,10,30,29,28,1,24,23,36,30,38,17,14,37])
    subseqAvgTime += time.time() - start
print subseqAvgTime/100.