import time
class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        res = 0
        for i in range(len(A)):
            res += 2**(i)*A[i]
            res -= 2**(len(A)-i-1)*A[i]
        return res%((10**9)+7)

A = []

print(len(A))
begin = time.time()
print(Solution().sumSubseqWidths(A))
print(time.time()-begin)