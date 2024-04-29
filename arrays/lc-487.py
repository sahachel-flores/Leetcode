  class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        """
        Solution I undestand
        """
        pre = -1
        curr = 0
        max_num = -1

        for i in nums:
            if i == 0:
                pre, curr = curr, 0
            else:
                curr += 1
            max_num = max(max_num, pre + 1 + curr)
        
        return max_num