# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Palindrome Linked List
    # TC: O(N)
    # SC: O(N), O(1) can be achieved but code becomes complex, more like medium type of problem
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l1 = []

        while head:
            l1.insert(0, head.val)
            head = head.next
        #print(l1)
        return l1 == l1[::-1]