# -*- coding: utf-8 -*-

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 双指针 Todo
        # Double pointer

        if len(nums) == 0:
            return 0
        i, j = 0, 1
        
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i += 1
        
        return i + 1




if "__main__" == __name__:
    solution = Solution()
    nums = [0,0,1,1,2,2,2,2,3,3,3,4,4,5]
    res = solution.removeDuplicates(nums)
    print(nums)
