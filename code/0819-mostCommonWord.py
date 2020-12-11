class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        the_most, count = '', 0

        words = []
        word = ''
        for i in paragraph:
            if i in '!?\',;. '.split():
                words.append(word)
                word = ''
            else:
                word += i
        print(words)




if "__main__" == __name__:
    solution = Solution()
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    print(solution.mostCommonWord(paragraph, banned))