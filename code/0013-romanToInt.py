# -*- coding: utf-8 -*-


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        _map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        ans, last = 0, 0
        length = len(s)
        
        for i in range(length):
            if i == 0:
                last, ans = _map[s[-1]], _map[s[-1]]  # 最后一个
                continue
            
            cur = _map[s[-1-i]] #当前

            if cur < last:
                ans -= cur
            else:
                ans += cur

            last = cur

        return ans









if "__main__" == __name__:
    solution = Solution()


    input1 = "III" # 3
    input2 = "IV" # 4
    input3 = "IX" # 9
    input4 = "LVIII" # 58
    input5 = "MCMXCIV" # 1994

    print(solution.romanToInt(input1))
    print(solution.romanToInt(input2))
    print(solution.romanToInt(input3))
    print(solution.romanToInt(input4))
    print(solution.romanToInt(input5))
    print(solution.romanToInt("I"))