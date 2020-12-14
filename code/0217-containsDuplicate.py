class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # 左移

        if n == 1:
            return True
        power = 0
        flag = True
        while flag:
            val = 2 << power
            if val == n:
                return True
            elif val > n:
                return False
            power += 1






if "__main__" == __name__:

    solution = Solution()
    
    n = 1025
    res = solution.isPowerOfTwo(n)
    print(res)