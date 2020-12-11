class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        ret, power = 0, 31

        while n:
            ret += (n & 1) << power # n & 1 means: 末位是1则是1, 0则是0 向右移位
            n = n >> 1  # n 左移移位
            power -= 1  # 位数-1
        return ret



if "__main__" == __name__:
    solution = Solution()
    res = solution.reverseBits(43261596)

    print(res)
