# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = []
        b = []
        while l1 !=None:
            a.append(l1.val)
            l1 = l1.next
        while l2 !=None:
            b.append(l2.val)
            l2 = l2.next
        c= int(''.join(a)) + int(''.join(b))
        s = str(c)
        l3 = ListNode(s[0])
        head = l3
        for i in range (1,len(s)):
            head = ListNode(s[i])
            head = head.next
        return l3