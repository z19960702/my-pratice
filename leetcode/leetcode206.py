
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prePoint = head
        nextPoint = head.next
        prePoint.next = None
        while (nextPoint != None):
            temp = nextPoint.next
            nextPoint.next = prePoint
            prePoint = nextPoint
            nextPoint = temp
        while (prePoint!=None):
            print (prePoint.val)
            prePoint = prePoint.next
        #return prePoint

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
Solution().reverseList(l)
                