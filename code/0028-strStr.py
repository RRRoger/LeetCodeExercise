# -*- coding: utf-8 -*-

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        L, n = len(needle), len(haystack)
        
        if L == 0:
            return 0
        
        start = 0
        
        while start < n - L + 1:
            curr_len = 0
            while curr_len < L and haystack[start] == needle[curr_len]:
                start += 1
                curr_len += 1
            if curr_len == L:
                return start - L
            start = start - curr_len + 1
        return -1


if "__main__" == __name__:
    solution = Solution()
    haystack = "helloo"
    needle = "lo"
    res = solution.strStr(haystack, needle)
    print("res", res)
