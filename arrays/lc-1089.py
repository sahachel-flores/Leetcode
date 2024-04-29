class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        My solution below seem to have a good performance
        """
        temp = 0
        zero = False
        pre =[]
        for i in range(len(arr)):
            #print(f"i is {i} current is {arr[i]} \nthe array is ", arr, "\n\n")
            if arr[i] == 0:
                zero = True
                pre.append(0)
            elif zero == False:
                continue
            temp = arr[i]
            arr[i] = pre[0]
            pre.pop(0)
            pre.append(temp)
            
        return arr