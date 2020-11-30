# -*- coding: utf-8 -*-


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        flag = 1
        if x < 0:
            flag = -1
            x = - x

        while x != 0:
            cur = x % 10
            ans = ans * 10 + cur
            x = x // 10

        ans = ans * flag

        # print("ans", ans)

        if -2 ** 31 <= ans <= 2 ** 31:
            return ans
        else:
            return 0

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
