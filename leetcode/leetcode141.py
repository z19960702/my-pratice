# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if (head == None):
            return False
        fast = head.next
        slow = head
        while (fast !=None):
            print(slow.val)
            if (fast == slow):
                return True
            else :
                slow = slow.next
                fast = fast.next
                if (fast != None and fast.next != None):
                    fast = fast.next
                else:
                    return False
        return False
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next = l.next
print (Solution().hasCycle(l))