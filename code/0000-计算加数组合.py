## -*- coding: utf-8 -*-

# 参考链接: https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie/hui-su-suan-fa-xiang-jie-xiu-ding-ban

import time

class Solution:

    """
    result = []
    def backtrack(路径, 选择列表):
        if 满足结束条件:
            result.add(路径)
            return

        for 选择 in 选择列表:
            做选择
            backtrack(路径, 选择列表)
            撤销选择
    """



    def calculate(self, k, n):
        ans = []
        nums = []

        all_nums = range(1, n)
        # print(all_nums)

        def backtrack(all_nums):
            if len(nums) == k:# and sum(nums) == n:
                ans.append(nums[:])
                return
            start = nums[-1] if nums else 0
            for r in range(start + 1, len(all_nums)):
                nums.append(all_nums[r])
                backtrack(all_nums[1:])
                nums.pop()

        backtrack(all_nums)


        return ans


if "__main__" == __name__:
    solution = Solution()
    k = 3
    n = 9
    res = solution.calculate(k, n)
    print(res)