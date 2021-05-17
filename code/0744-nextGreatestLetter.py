# https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/submissions/

# i cant understand what the problem means


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for c in letters:
            if c > target:
                return c
        return letters[0]


if "__main__" == __name__:
    solution = Solution()

    letters = ["c", "f", "j"]

    target = "d"

    print(solution.nextGreatestLetter(letters, target))
