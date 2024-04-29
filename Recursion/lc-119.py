class Solution:
    # This solution for pascal triangel 2 using an equation
    # TC: O(N)
    # SC O(N)
    class Solution:
    def getRow(self, n):
        row = [1]
        for k in range(1, n + 1):
            row.append(int((row[-1] * (n - k + 1)) / k))
        return row
    # getNum(rowIndex,colIndex)=getNum(rowIndex−1,colIndex−1)+getNum(rowIndex−1,colIndex)
    # TC: O(2^k) where K are the colunms 0 to K 
    # SC: O(K)
    class Solution:
    def getNum(self, row, col):
        if col == 0 or row ==0 or col==row:
            return 1
    
        return  self.getNum(row-1, col-1) + self.getNum(row-1,col)
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex+1):
            ans.append(self.getNum(rowIndex, i))
        return ans
        