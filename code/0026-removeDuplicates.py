# -*- coding: utf-8 -*-

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 本题判断的是nums的内容
        # 无关返回值

        new_nums = nums[:1]
        # print(new_nums)
        for i in range(len(nums)):
            if i == 0:
                continue
            if nums[i] == new_nums[-1]:
                continue
            else:
                new_nums.append(nums[i])
        nums[:] = new_nums
        print(nums)




if "__main__" == __name__:
    solution = Solution()
    nums = []

    res = solution.removeDuplicates(nums)
    print(res)