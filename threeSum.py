class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(self.threeSumHelper(nums, []))

    def threeSumHelper(self, nums, listSoFar):
        if len(listSoFar) + len(nums) <3:
            return set()
            
        if len(listSoFar) == 3:
            if sum(listSoFar) == 0:
                listSoFar.sort()
                tupListSoFar = tuple(listSoFar)
                retSet = set()
                retSet.add(tupListSoFar)
                return retSet
            else:
                return set()

        if len(nums) == 0:
            return set()

        set1 = self.threeSumHelper(nums[1:], listSoFar)
        newListSoFar = listSoFar + [nums[0]]
        set2 = self.threeSumHelper(nums[1:], newListSoFar)
        
        return set1|set2

nums = [-1, 0, 1, 2, -1, -4]
print Solution().threeSum(nums)