'''Problem: Set_Matrix_Zeroes'''

#CODE : 

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if matrix==None or len(matrix)==0:
             return 
         
        # use first col and row as buffer to hold a flag to check if accordinate col or row should be 0
        # before do that, declare two flag used to check if first col and row need be change to 0 at the end
        first_row_to_zero=False
        first_col_to_zero=False
        
        # check the if first row and first col need to be changed to 0 at end   
        if matrix[0][0]==0:
            first_row_to_zero=True
            first_col_to_zero=True
        else:
            if 0 in matrix[0]:
                first_row_to_zero=True
            if len([matrix[x][0] for x in range(0, len(matrix)) if matrix[x][0]==0])>0:
                first_col_to_zero=True
                
        # if find a cell with 0 then set accordinate first row and col to set as a flag 
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
                    
        # base on the all the flag in first row and col set 0 to the cell  
        for i in range (1, len(matrix)):
            for j in range(1, len(matrix[0])):
                 if matrix[0][j]==0 or matrix[i][0]==0:
                     matrix[i][j]=0
        
        # use pre-marked flag to decide if first row and col need to be changed to 0
        if first_row_to_zero:
            for i in range(0, len(matrix[0])):
                matrix[0][i]=0
        if first_col_to_zero:
            for i in range (0, len(matrix)):
                matrix[i][0]=0

                
                
                
                
                #or solution 2 

                
                
                
                
# with O(rows+cols) extra space
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if matrix==None or len(matrix)==0:
            return
        cols=[False]*len(matrix[0])
        rows=[False]*len(matrix)
        
        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                if matrix[row][col]==0:
                    cols[col]=True
                    rows[row]=True
        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                if cols[col] or rows[row]:
                    matrix[row][col]=0
