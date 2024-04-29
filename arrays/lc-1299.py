class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        I had to look at this solution
        """
        right_max = -1

        for i in range(len(arr)-1, -1, -1):
            #print(f'i: {i}, arr[i]: {arr[i]} right_max: {right_max} \n {arr} \n' )
            new_max = max(arr[i], right_max)
           
            arr[i] = right_max

            right_max = new_max
        
        return arr