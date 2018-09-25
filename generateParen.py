import inspect 

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.penis(n, 0, "")
    
    
    def penis(self, n, openParen, strSoFar):
        print inspect.getargvalues(inspect.currentframe())

        print "strSoFar: ", strSoFar
        if n == 0:
            for i in range(openParen):
                strSoFar += ")"
            return set([strSoFar])

        strSoFar += "("
        res = set()
        res |= self.penis(n-1, openParen+1, strSoFar)
        
        print "res from the first recursive call:", res

        for i in range(openParen+1):
            strSoFar += ")"
            #print strSoFar, "openParen: ", openParen-i
            res |= self.penis(n-1, openParen-i, strSoFar)

        print "end of function"

        return res


print Solution().generateParenthesis(3)