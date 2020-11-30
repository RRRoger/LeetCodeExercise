# Definition for singly-linked list.
# -*- coding: utf-8 -*-

# 链表的知识还需要继续加强

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def __str__(self):
        delimeter = '->'
        flag = True
        res = []
        def toString(obj, res):
            res.append(obj.val)
            if obj.next:
                return toString(obj.next, res)
            return res
        res = toString(self, res)
        return delimeter.join(map(str, res))



class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # 判断空的情况
        if not l1:
            return l2
        if not l2:
            return l1


        # 拼接字典, 待优化
        res = []
        while l1 and l2:
            if l1.val < l2.val:
                res.append(l1.val)
                l1 = l1.next
            else:
                res.append(l2.val)
                l2 = l2.next

        a = ListNode(res[-1])
        for i in range(len(res)):
            if i == (len(res)-1):
                break
            a = ListNode(res[-i-2], a)


        l = l1 or l2

        def _last(obj):
            """ 返回最后一个节点 """
            if not obj.next:
                return obj
            else:
                return _last(obj.next)

        last = _last(a)
        # print(last)
        last.next = l

        return a





if "__main__" == __name__:
    solution = Solution()

    l = ListNode(4)
    l = ListNode(2, l)
    l = ListNode(1, l)
    # print(l3)

    r = ListNode(6)
    r = ListNode(4, r)
    r = ListNode(3, r)
    r = ListNode(1, r)
    r = ListNode(1, r)
    r = ListNode(0, r)
    # print(r3)

    print(solution.mergeTwoLists(r, None))





