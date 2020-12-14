class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (-n) == n


if "__main__" == __name__:

    solution = Solution()
    
    n = 1024
    res = solution.isPowerOfTwo(n)
    print(res)