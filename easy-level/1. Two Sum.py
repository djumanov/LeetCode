class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)-1):
            temp = nums[i]
        
            for j in range(i+1, len(nums)):
                temp += nums[j]
                if temp == target:
                    res = [i, j]
                    break
                else:
                    temp = nums[i]
        return res