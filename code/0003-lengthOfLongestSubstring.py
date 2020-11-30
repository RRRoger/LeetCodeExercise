# -*- coding: utf-8 -*-

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        print(st)
        return ans




if __name__ == "__main__":

    solution = Solution()
    s = "abcba"

    print(solution.lengthOfLongestSubstring(s))
        


