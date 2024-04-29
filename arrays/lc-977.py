class Solution:
  class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        # first solution I came up with
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums = nums.sort()
        return nums
        """
        return sorted(i*i for i in nums)