# -*- coding: utf-8 -*-
import time

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0

        nums = []

        if n == 0:
            return

        while 1:
            if i + 1 > m:
                if j == n:
                    break
                nums.append(nums2[j])
                j += 1
                continue

            if j + 1 > n:
                nums.append(nums1[i])
                i += 1
                continue

            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        nums1[:] = nums
        print(nums1)




if "__main__" == __name__:
    solution = Solution()
    nums1 = [2,5,6,7,11,12,13,15,0,0,0]
    nums2 = [2,5,6,7,11,12,13,15]
    m = 8
    n = 8

    # nums1 = [2,0]
    # nums2 = [1]
    # m = 1
    # n = 1

    res = solution.merge(nums1, m, nums2, n)
    print(res)
