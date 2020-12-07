class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def build(s):
            stack = list()
            for i in s:
                if i != '#':
                    stack.append(i)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        if build(S) == build(T):
            return True
        return False








if __name__ == "__main__":

    solution = Solution()

    s1 = "ab#c"
    t1 = "ad#c"

    print(solution.backspaceCompare(s1, t1))
    # print(solution.backspaceCompare(s2))