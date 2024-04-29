class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        #solution I came up with, however using strings we can find an optimized solution
        temp = 10
        rc = 0
        for i in nums:
            temp = 0
            while int(i) != 0:
                temp += 1
                i = i/10
            if temp % 2 == 0:
                rc += 1
        return rc
    """
    #optimazed solution from leetcode
    class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if len(str(i))%2==0:
                count+=1
        return count
    """