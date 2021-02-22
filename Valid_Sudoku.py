'''Problem : VALID SUDOKU 
'''


#CODE:
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHashTable, columnHashTable, boxHashTable = [], [], []
        rowLimit, columnLimit = len(board), len(board[0])
        for i in range(rowLimit):
            rowHashTable.append(set()) # Per each row
            columnHashTable.append(set()) # Per each column
            boxHashTable.append(set()) # Per each box
        def getBoxIndex(row, column):
            return row // 3 * 3 + column // 3        
        for row in range(rowLimit):
            for column in range(columnLimit):
                if board[row][column] == '.':
                    continue
                if board[row][column] in rowHashTable[row]:
                    return False
                rowHashTable[row].add(board[row][column])
                if board[row][column] in columnHashTable[column]:
                    return False
                columnHashTable[column].add(board[row][column])
                boxNum = getBoxIndex(row, column)
                if board[row][column] in boxHashTable[boxNum]:
                    return False
                boxHashTable[boxNum].add(board[row][column])
        return True
