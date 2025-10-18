class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsLen, left, result = len(nums), 0, 0
        nums = sorted(nums)
        for i in range(numsLen):
            while left < i and nums[i] - nums[left] > 1L:
                left += 1
            if nums[i] - nums[left] == 1L:
                result = max(i - left + 1, result)
        return result
