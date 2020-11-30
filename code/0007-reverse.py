# -*- coding: utf-8 -*-


class Solution(object):
    def reverse(self, x):
        """
            用字符串处理
        :type x: int
        :rtype: int
        """
        
        string = str(x)
        x = 1
        if string.startswith('-'):
            string = string[1:]
            x = -1

        ans = x * int(string[::-1])

        if ans >= 2 ** 31:
            return 0
        if ans < -1 * (2 ** 31):
            return 0

        return ans



if "__main__" == __name__:
    solution = Solution()
    input1 = 123
    input2= -123
    input3 = 120

    # 2 ** 31 = 2147483648

    input4 = 2147483648
    1534236469
    input5 = -2147483649

    input6 = 2147483647
    input7 = -2147483648
    print(solution.reverse(input1))
    print(solution.reverse(input2))
    print(solution.reverse(input3))
    print(solution.reverse(input4))
    print(solution.reverse(input5))
    print(solution.reverse(input6))
    print(solution.reverse(input7))

    print(solution.reverse(1534236469))
