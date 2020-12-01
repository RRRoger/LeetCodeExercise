# -*- coding: utf-8 -*-

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # 使用python的切片

        length = len(needle)
        for i in range(len(haystack) - length + 1):
            if haystack[i:i+length] == needle:
                return i
        return -1





if "__main__" == __name__:
    solution = Solution()
    haystack = "helloo"
    needle = "helloo"
    res = solution.strStr(haystack, needle)
    print("res", res)
