class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        ans = set()
        ctizen = set()
        for el in trust:
            ctizen.add(el[0])
            if el[0] in ctizen:
                ans.remove(el[0])
            else:
                ans.add(el[0])
        print ans






if __name__ == "__main__":

    solution = Solution()

    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]

    print(solution.findJudge(3, trust))
    # print(solution.backspaceCompare(s2))