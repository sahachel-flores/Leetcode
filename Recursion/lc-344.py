class Solution:
    def reverseString(self, s: List[str]) -> None:
        #approach 1: Recursion, in place using 2 pointer method
        # TC: we have N/2 swaps thus -> O(n) 
        # SC: O(N) to keep recursion stack 
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left+1, right-1)
        
        helper(0, len(s)-1)



class Solution:
    def reverseString(self, s: List[str]) -> None:
        #approach 2: Two pointers, iteration 
        # TC: Still the same as before N/2 -> O(N)
        # SC: We see am improved SC of O(1) compare to recursion approach 
        # Note: solution is similar to the one before, we are just saving the extra function calls 

        left = 0
        right = len(s) -1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
