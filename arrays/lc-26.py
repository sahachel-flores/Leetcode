class Solution:
    """
    Solution I came up with
    """
    def removeDuplicates(self, nums: List[int]) -> int:
      
        if len(nums) == 0:
            return
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1
            
   
        return index