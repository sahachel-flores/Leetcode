class Solution:
    #Approach below has a time complexity of O(N + M) where N and M are the lenghts of listA and listB
    #Using the 2 pointer approach 
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listA = set()

        while headA:
            listA.add(headA)
            headA = headA.next
        while headB:
            if headB in listA:
                return headB
            headB = headB.next
        return None
    
# Two pointer solution
class Solution:
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    pA = headA
    pB = headB

    while pA != pB:
        pA = headB if pA is None else pA.next
        pB = headA if pB is None else pB.next

    return pA
    # Note: In the case lists do not intersect, the pointers for A and B
    # will still line up in the 2nd iteration, just that here won't be
    # a common node down the list and both will reach their respective ends
    # at the same time. So pA will be NULL in that case.