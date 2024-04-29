# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
# The solution below has TC O(2L-n) = O(L), and SC = O(1), 
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy_node = ListNode(None)
        dummy_node.next = head
        slow = dummy_node
        fast = head
        

        while n>0 and fast:
            fast = fast.next
            n=n-1

        while fast:
            fast=fast.next
            slow=slow.next

        slow.next = slow.next.next

        return dummy_node.next
# Two pointer solution I came up with
# TC = O(L)
# SC - O(1)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        first = dummy
        second = dummy

        i = 0
        while first:
            if i > n:
                second = second.next
            first = first.next
            i+=1
        second.next = second.next.next

        return dummy.next