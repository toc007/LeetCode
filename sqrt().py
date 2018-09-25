class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        for i in range(x):
            if i*i > x:
                return i-1
            elif i*i == x:
                return i

print Solution().mySqrt(2147395599)
