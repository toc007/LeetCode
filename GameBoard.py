class piece(object):
    def __init__(self, validPieces):
        self.validPieces = validPieces

class board(object):
    def __init__(self, length, width, defPiece):
        self.length = length
        self.width = width
        self.board = [[defPiece for i in range(width)] for j in range(length)]
    
    def __str__(self):
        strRep =""
        for l in self.board:
            for w in l:
                strRep += "|" + str(w)
            strRep += "|\n"
        return strRep

                


brd = board(3,3,None)
print str(brd)
