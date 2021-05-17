class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = map(int, str(n))
        ans = 0
        for num in nums:
            ans += num ** 2
        if ans == 1:
            return True
        else:
            return self.isHappy(ans)

            



if "__main__" == __name__:

    solution = Solution()
    
    n = 11
    res = solution.isHappy(n)
    print(res)
