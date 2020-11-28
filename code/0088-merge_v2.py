# -*- coding: utf-8 -*-


# 双指针 / 从前往后
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        i = 0 
        j = 0
        nums = []

        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        while i < m and j < n: 
            if nums1[i] < nums2[j]: 
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        # if there are still elements to add
        if i < m: 
            nums += nums1[i:m]
        if j < n:
            nums += nums2[j:n]

        nums1[:] = nums





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
    print(nums1)
    print(res)
