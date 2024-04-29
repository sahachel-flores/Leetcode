class Solution:
    """
    Brute force I came up with, I first attemped w/out using sets and my code would finish running 
    because it would get hang with a testcase which contained many duplicates. With set() I eliminate the duplicate solutions, which help me run faster through my code
    """
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #code with beteer time complexity and less code
        l = set()
        #imporve with code below, to eliminate for loop
        #l = set(range(1,len(nums)+1))
        
        for i in range(1,len(nums)+1):
            l.add(i)
        return l - set(nums)
        
        """""
        nums_set = set(nums)
        rc = []
        i = 1
        while i <= len(nums):
            if i not in nums_set:
                rc.append(i)
        """