class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        
        stack = []

        for i in range(len(ops)):

            if ops[i] == 'D':
                stack.append(stack[-1] * 2)
            elif ops[i] == '+':
                stack.append(stack[-1] + stack[-2])
            elif ops[i] == 'C':
                stack.pop()
            else:
                stack.append(int(ops[i]))
        
        return sum(stack)







if __name__ == "__main__":

    solution = Solution()
    ops1 = ["5","2","C","D","+"]
    ops2 = ["5","-2","4","C","D","9","+","+"]

    print(solution.calPoints(ops1))
    print(solution.calPoints(ops2))