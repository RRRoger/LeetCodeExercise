# -*- coding: utf-8 -*-

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 在归并排序的时候 排到一半的时候
        # 取中位数, 后面的不排序了
        i = 0
        j = 0
        m = len(nums1)
        n = len(nums2)
        length = m + n
        nums = []
        while len(nums) <= (length // 2 + 1):
            while i < m and j < n:
                if nums1[i] < nums2[j]:
                    nums.append(nums1[i])
                    i += 1
                else:
                    nums.append(nums2[j])
                    j += 1
            if i < m: 
                nums += nums1[i:m]
            if j < n:
                nums += nums2[j:n]

        if length % 2 == 0:
            res = (nums[length // 2] + nums[length // 2 - 1]) / 2.0
        else:
            res = nums[length // 2]
        print(nums)
        return res






if "__main__" == __name__:
    solution = Solution()
    nums1 = [1,3]
    nums2 = [2, 4]
    res = solution.findMedianSortedArrays(nums1, nums2)
    print(res)
