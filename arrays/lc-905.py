class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        Solution I came up with, has good run time, but uses more memory
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums