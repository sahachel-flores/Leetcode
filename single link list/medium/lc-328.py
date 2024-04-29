# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Solution for odd-even linked list
    # TC: O(N)
    # SC: O(1)
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #current 
        head1 = odd = ListNode()
        head2 = even = ListNode()

        #current node with i number
        i = 1
        curr = head
        
        while curr:
            if i%2 == 0:
                even.next = curr
                even = even.next
            else:
                odd.next = curr
                odd = odd.next
                
            i += 1
            curr = curr.next
        even.next = None
        odd.next = head2.next

        return head1.next