## -*- coding: utf-8 -*-

# 参考链接: https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie/hui-su-suan-fa-xiang-jie-xiu-ding-ban

import time

class Solution:

    """
    result = []
    def backtrack(路径, 选择列表):
        if 满足结束条件:
            result.add(路径)
            return

        for 选择 in 选择列表:
            做选择
            backtrack(路径, 选择列表)
            撤销选择
    """

    def letterCombinations(self, digits):
        if not digits: return []
        
        dic = {
            '2':'abc', 
            '3':'def', 
            '4':'ghi', 
            '5':'jkl', 
            '6':'mno', 
            '7':'pqrs', 
            '8':'tuv', 
            '9':'wxyz'
        }
        
        ans = []
        path = []

        def backtrack(s): 
            time.sleep(1)

            if len(path) == len(digits):
                print("*" * 20, path)
                ans.append(''.join(path[:]))
                return 

            for c in dic[s[0]]:
                path.append(c)
                print('after append', path)
                backtrack(s[1:])
                path.pop()
                print('after pop', path)
        
        backtrack(digits)
        return ans


if "__main__" == __name__:
    solution = Solution()

    res = solution.letterCombinations("234")
    print(res)