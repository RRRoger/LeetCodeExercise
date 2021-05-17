# Definition for singly-linked list.
# -*- coding: utf-8 -*-

# 链表的知识还需要继续加强

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
    
    # 哨兵节点方案: https://leetcode-cn.com/problems/remove-linked-list-elements/solution/yi-chu-lian-biao-yuan-su-by-leetcode/
    def removeElements(self, head, val):
        sentinel = ListNode(0)
        sentinel.next = head
        
        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return sentinel.next




if "__main__" == __name__:
    solution = Solution()

    nums = map(int, "1->2->6->3->4->5->6".split("->"))
    nums = generate_node(nums)
    print(nums)
    val = 6
    res = solution.removeElements(nums, val)
    print(res)