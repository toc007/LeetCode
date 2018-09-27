def getMatchingGroups(grid1, grid2):
    print getGroups(getOnes(grid1)).intersection(getGroups(getOnes(grid2)))

def getOnes(grid):
    res = set()
    for (row, r) in enumerate(grid):
        for (col, c) in enumerate(r):
            if c == "1":
                res.add((row, col))
    return res

def getGroups(coordSet):
    res = set()
    while len(coordSet) > 0:
        startCoord = coordSet.pop()
        res.add(frozenset(bfs(startCoord, coordSet)))

    return res

def bfs(startCoord, coordSet):
    res = set()
    pending = [startCoord]
    while len(pending) > 0:
        working = pending.pop()
        x, y = working
        top = (x-1, y)
        bot = (x+1, y)
        left = (x, y-1)
        right = (x, y+1)
        if top in coordSet:
            pending.append(top)
            coordSet.remove(top)
        if bot in coordSet:
            pending.append(bot)
            coordSet.remove(bot)
        if left in coordSet:
            pending.append(left)
            coordSet.remove(left)
        if right in coordSet:
            pending.append(right)
            coordSet.remove(right)

        res.add(working)

    return res

grid1 = [
    "101", 
    "110", 
    "001"
    ]

grid2 = [
    "101", 
    "110", 
    "001"
    ]

getMatchingGroups(grid1, grid2)