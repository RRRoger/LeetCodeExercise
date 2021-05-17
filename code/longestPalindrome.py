class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 动态规划，dp[i][j]表示s[i:j]是否为回文子串
        # 每次判断s[i][j]时更新maxlen=j-i+1和start=i
        # 边界，当j-i+1<2时，肯定是回文串
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        # print(dp)

        start, max_len = 0, 1

        # 边界
        if n < 2:
            return s
        # 初始化
        for i in range(n):
            dp[i][i] = True

        # print(dp)
        # 枚举区间终点
        for j in range(1, n):
            # 枚举起点
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                
                if dp[i][j]:
                    l = j - i + 1
                    if l > max_len:
                        max_len = l
                        start = i

        return s[start: start+max_len]

if "__main__" == __name__:
    solution = Solution()

    print(solution.longestPalindrome("absjaskdjahsabcdefgfedcba"))
