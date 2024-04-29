# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #firs solution using recursion
    # TC: O(N)
    # SC: O(N) due to stack space utilized for recursion
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        #nodes to be swap
        first_node = head
        second_node = head.next

        #swapping
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        #head is now the second node
        return second_node

#better solution
class Solution:
    #firs solution using recursion
    # TC: O(N)
    # SC: O(1), we are not using additional space
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        pre_node = dummy

        while head and head.next:
            #nodes to swap 
            first_node = head
            second_node = head.next

            #Swapping
            pre_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            #adjusting pre and head
            pre_node = first_node
            head = first_node.next
        return dummy.next