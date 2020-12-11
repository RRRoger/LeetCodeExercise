class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0

        ans = 1
        for i in range(n):
            ans *= (i+1)
        return ans


if "__main__" == __name__:
    solution = Solution()
    print(solution.trailingZeroes(-5))
