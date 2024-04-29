class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        hash_map = set()
        temp = head
        while temp.next:
            if temp in hash_map:
                return temp
            hash_map.add(temp)
            temp = temp.next
        return None