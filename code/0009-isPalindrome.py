# -*- coding: utf-8 -*-


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        i = 0

        def _isPalindrome(i):

            if len(string) % 2 == 0 and (len(string) // 2 == i):
                return True
            elif len(string) % 2 == 1 and (len(string) // 2 + 1 == i):
                return True

            if string[i] == string[-1-i]:
                i += 1
                return _isPalindrome(i)                
            else:
                return False
        return _isPalindrome(i)
        



if "__main__" == __name__:
    solution = Solution()

    print(solution.isPalindrome(100313001))

