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
