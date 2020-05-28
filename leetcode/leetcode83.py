# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = head
        if (head == None):
            return  None
        while head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        while pre !=None:
            print (pre.val) 
            pre = pre.next
            

l = ListNode(1)
l.next = ListNode(1)
l.next.next = ListNode(2)
Solution().deleteDuplicates(l)