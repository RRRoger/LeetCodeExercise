# # -*- coding: utf-8 -*-

# Definition for singly-linked list.

# 使用递归的方案

def generate_node(_list):
    if not _list:
        return None
    r = ListNode(_list[-1])
    for i in range(1, len(_list)):
        r = ListNode(_list[-1-i], r)
    return r

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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        
        def link(this, res):
            if this:
                res = ListNode(this.val, res)
                return link(this.next, res)
            return res

        res = ListNode(head.val)
        return link(head.next, res)




            



if __name__ == '__main__':
    solution = Solution()
    r = generate_node([5,4,3,2,1])
    # print(r)
    res = solution.reverseList(r)
    print(res)


