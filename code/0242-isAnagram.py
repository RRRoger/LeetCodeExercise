class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if len(s) != len(t):
        #     return False

        char_dict = {}
        for i in s:
            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1

        for i in t:
            
            if i in char_dict:
                char_dict[i] -= 1
            else:
                return False

        return all(map(lambda x: not char_dict[x], char_dict))



if "__main__" == __name__:

    solution = Solution()
    
    s = "anagramm"
    t = "nagarammx"


    res = solution.isAnagram(s, t)
    print(res)
