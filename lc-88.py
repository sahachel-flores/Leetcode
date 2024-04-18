class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        This is the solution I came up with, there is a better way to do it as runtime of this solution is pretty bad (beats 5%)
        """
        for i in range(len(nums1)):
            print(f"i = {i} and arr1 is {nums1} and arr2 is ", nums2)
            
            if len(nums2) == 0:
                print("breaking")
                break
            print(f"Comparing {nums1[i]} and {nums2[0]} m is {m}")
            
            if (nums1[i] <= nums2[0]) and (m > 0):
                print("Continue\n")
                m -= 1
                continue
            else: 
                nums1.insert(i,nums2[0])
                nums2.pop(0)
                nums1.pop(-1)
                
                print("do something\n")
        print("returning")
        return nums1
    
    """
    #most optimal solution, depends on a sort function to achieve its goal
    class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        result = []
        ind = 0
        for i in range(m, m+n):
            nums1[i]=nums2[ind]
            ind = ind + 1
        print(nums1.sort())    
    
    """
    


