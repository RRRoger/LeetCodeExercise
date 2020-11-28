# -*- coding: utf-8 -*-

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        # num = list(set(sorted(num)))
        num= sorted(num)
        length = len(num)
        # print(length)
        # print(num)
        # print(len(num) % 2)
        if length % 2 == 0:
            # 偶数
            return (num[length/2-1] + num[length/2])/2.0
        else:
            # 奇数
            return num[(length+1)/2-1]





if "__main__" == __name__:
    solution = Solution()
    nums1 = [0,0,0,0,0]
    nums2 = [-1,0,0,0,0,0,1]
    res = solution.findMedianSortedArrays(nums1, nums2)
    print(res)
