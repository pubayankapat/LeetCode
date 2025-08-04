class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        First_row_zero = False
        First_col_zero = False
        # checking if the first has zero or not
        for c in range(col):
            if matrix[0][c] == 0:
                First_row_zero = True
                break
        # checking if the first column has zero or not 
        for r in range(row):
            if matrix[r][0] == 0:
                First_col_zero = True
                break
        # setting the first row as note if the column has zero in it
        for r in range(1,row):
            for c in range(1,col):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        # setting zeroes to rows marked as zeroes
        for r in range(1,row):
            if matrix[r][0] == 0:
                for c in range(1,col):
                    matrix[r][c] = 0
                
            
        # setting zeroes to columns marked as zeroes
        for c in range(1,col):
            if matrix[0][c] == 0:
                for r in range(1,row):
                    matrix[r][c] = 0

            

         # set the first row to zero if needed
        if First_row_zero:
            for c in range(col):
                matrix[0][c] = 0

        # set the first column to zero if needed
        if First_col_zero:
            for r in range(row):
                matrix[r][0] = 0
            






        
        
       
        