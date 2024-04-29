class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
        Solution I came up with, this solution can be improved 
        """
        if len(arr) < 3:
            return False
        else:
            pre = arr[0]
            found_max = False
            max_value = -1
            for i in range(1,len(arr)):
                #print(f' maxVal {max_value} and current: {arr[i]} pre: {pre} and found max: {found_max} ')
                if found_max:
                    if pre > arr[i] and max_value > arr[i] and max_value > arr[0]:
                        pre = arr[i]
                        continue
                    else:
                        return False
                if pre < arr[i]:
                    pre = arr[i]
                    continue
                elif pre > arr[i]:
                    max_value = pre
                    pre = arr[i]
                    found_max = True
                else:
                    return False
        if max_value == -1:
            return False
        return True
                
                
                