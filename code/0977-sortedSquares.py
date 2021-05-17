class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(r ** 2 for r in nums)


if "__main__" == __name__:
    solution = Solution()

    nums = [-4,-1,0,3,10]

    res = solution.sortedSquares(nums)
    print(res)

