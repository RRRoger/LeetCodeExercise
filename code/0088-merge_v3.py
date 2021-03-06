# -*- coding: utf-8 -*-


# 双指针 / 从后往前
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1
        
        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] =  nums1[p1]
                p1 -= 1
            p -= 1

            # print("p", p)
            # print("p1", p1)
            # print("p2", p2)
        
        # add missing elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]






if "__main__" == __name__:
    solution = Solution()
    nums1 = [1,3,6,7,10,12,14,17,0,0,0,0,0,0,0,0]
    nums2 = [2,5,6,7,11,12,13,15]
    m = 8
    n = 8

    # nums1 = [2,0]
    # nums2 = [1]
    # m = 1
    # n = 1

    res = solution.merge(nums1, m, nums2, n)
    print(nums1)
    print(res)
