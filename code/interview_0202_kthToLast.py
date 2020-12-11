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
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        if not head: return None
        _list = [head.val]
        while head.next:
            _list.append(head.next.val)
            head = head.next
        return _list[-k]





if __name__ == '__main__':
    solution = Solution()
    r = generate_node([4,5,1,9])
    res = solution.kthToLast(r,2)
    print(res)