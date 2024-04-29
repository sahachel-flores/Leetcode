class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Solution I came up with, better solution below
        """
        index = 0
        left = 0
        right = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                #index = i
                continue
            else:
                nums[index] = nums[i]
                index += 1
        print(nums, " ", index)     
        if index < (len(nums)):
            for j in range(index, len(nums)):
                nums[j] = 0
        return nums
    
    """
    class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
        return nums
    
    """