# -*- coding: utf-8 -*-

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
        # print(res)
        return delimeter.join(map(str, res))


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = set()
        this_node = head
        
        while this_node.next:
            a.add()
            



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


    print(solution.deleteDuplicates(r))



