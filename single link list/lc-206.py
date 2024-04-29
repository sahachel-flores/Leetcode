# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # This solution has reverse a liunked list 
    # TC: O(N) where N=linked list size
    # SC: O(1) constant
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 2 3 4 5
        #pre=
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
# A solution using recursion, SC performs worst due to increating size of stack
# TC: O(N)
# SC: O(N)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next):
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p