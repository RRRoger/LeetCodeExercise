class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res, power = 0, 31
        while n:
            res += (n & 1) << power
            n = n >> 1
            power -= 1
            print(power)
        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.reverseBits(0b0000000000000000000000011000000)
    print(bin(res))
