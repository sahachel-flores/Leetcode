class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        hash_map = set()
        temp = head
        while temp.next:
            if temp in hash_map:
                return True
            hash_map.add(temp)
            temp = temp.next
        return False
    
    #solution below uses 2 pointer method, it has the same time compplexity as above O(n),
    #however the space complexity is O(1) because we are using 2 pointer for storage  
    """
    class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
    """
