# -*- coding: utf-8 -*-


class Solution:
    def isValid(self, s):

        # 长度奇数返回False
        if len(s) % 2 == 1:
            return False
        
        _map = {
            "]": "[",
            ")": "(",
            "}": "{",
        }

        stack = []

        for ch in s:
            if ch in _map:
                if not stack:
                    return False
                elif stack[-1] != _map[ch]:
                    # print(stack)
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)
        return not stack




if "__main__" == __name__:
    solution = Solution()
    input1 = "()"
    input2 = "()[]{}"
    input3 = "(]"
    input4 = "([)]"

    # print(solution.isValid(input1))
    # print(solution.isValid(input2))
    # print(solution.isValid(input3))
    # print(solution.isValid(input4))

    x = "{[]}{[]}{[][}{][]}{[]}"
    print(solution.isValid(x))


    
