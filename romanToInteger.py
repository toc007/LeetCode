class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        accum = 0
        for i in range(len(s)-1, -1, -1):
        	if s[i] == 'I':
        		if accum >= 5:
        			accum -= 1
        		else:
        			accum +=1
        	elif s[i] == 'V':
        		accum += 5
        	elif s[i] == 'X':
        		if accum >= 50:
        			accum -= 10
        		else:
        			accum +=10
        	elif s[i] == 'L':
        		accum += 50
        	elif s[i] == 'C':
        		if accum >= 500:
        			accum -= 100
        		else:
        			accum +=100
        	elif s[i] == 'D':
        		accum += 500
        	elif s[i] == 'M':
        		accum += 1000
        return accum
