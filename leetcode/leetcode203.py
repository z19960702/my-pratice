class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:   
        temp = head
        pre = None
        while temp != None:
            if temp.val == val:
                if (temp.next != None):
                   temp.val =  temp.next.val
                   temp.next =  temp.next.next
                else:
                    pre.next = None
                    break
            else :
                pre = temp
                temp = temp.next
        while head!=None:
            print (head.val)
            head = head.next
        return head

l = ListNode(1)
s = None
Solution().removeElements(l,1)
