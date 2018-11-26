class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        self.n,self.m = len(matrix),len(matrix[0])
        self.matrix = [[0]*self.m for _ in range(self.n)]
        self.BIT = [[0]*(self.m+1) for _ in range(self.n+1)]
        for i in range(self.n):
            for j in range(self.m):
                self.update(i,j,matrix[i][j])

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        y = row+1
        while y < self.n + 1:
            x = col + 1
            while x < self.m + 1:
                self.BIT[y][x] += diff
                x += x&-x
            y += y&-y
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.cornerSum(row2,col2) - 
               self.cornerSum(row1-1,col2) -
               self.cornerSum(row2,col1 -1) + 
                self.cornerSum(row1-1,col1-1)
        
    def cornerSum(self,row,col):
        ans, y = 0, row + 1
        while y > 0:
            x = col + 1
            while x > 0:
                ans += self.BIT[y][x]
                x -= x&-x
            y -= y&-y
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)