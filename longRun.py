#!/usr/bin/python

# longRun defined as m roses in a row
# find latest date where there are k longRuns
# arr contains the date at which each rose bush will bloom
#   ex. [1,5,2,6,7,3,4,7,8,3,4,7]
#       rose bush 1 will bloom on the 1st day
#       rose bush 3 will bloom on the 2nd day
def longRun(arr, k, m):
    if len(arr) < k*m or len(arr) < m:
        return 0
    maxDateInArr = max(arr)
    beginIndex = 0
    endIndex = arr.index(maxDateInArr)
    longRuns = 0

    while True:
        
        if endIndex-beginIndex >= m:
            longRuns += 1

            print("long run from %d to %d" % (beginIndex, endIndex))
            print(arr[beginIndex:endIndex], "\n")

            beginIndex = endIndex+1
        try:
            endIndex = arr.index(maxDateInArr, beginIndex)
        except ValueError as e:
            break

    if longRuns == k:
        return maxLongRunDate
    else:
        return 0

longRun([1,5,2,6,7,3,4,7,8,3,4,7], 2, 3)