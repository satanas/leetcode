# Iterate the whole matrix (nested for loop)
# For each zero, mark the first row and the first column (if not marked already)
# At the end of the iteration, iterate first row and put zeros in all the columns marked
# Then iterate the first column and put zeroes in all the rows marked


# [8,3,6,9,7,8,0,6]
# [0,3,7,0,0,4,3,8]
# [5,3,6,7,1,6,2,6]
# [8,7,2,5,0,6,4,0]
# [0,2,9,9,3,9,7,3]

# [B,3,6,9,7,8,C,6]
# [R,3,7,0,0,4,3,8]
# [5,3,6,7,1,6,2,6]
# [8,7,2,5,0,6,4,0]
# [0,2,9,9,3,9,7,3]

# [B,3,6,C,C,8,C,C]
# [R,3,7,0,0,4,3,8]
# [5,3,6,7,1,6,2,6]
# [R,7,2,5,0,6,4,0]
# [R,2,9,9,3,9,7,3]

class Solution:
    CLEAR_COL = "C"
    CLEAR_ROW = "R"
    CLEAR_BOTH = "B"

    def setZeroes(self, matrix):
        # TODO: Input validation

        for i in range(len(matrix)): # 1,0
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if matrix[i][0] == "C":
                        matrix[i][0] = "B"
                    elif matrix[i][0] != "B":
                        matrix[i][0] = "R"

                    if matrix[0][j] == "R":
                        matrix[0][j] = "B"
                    elif matrix[0][j] != "B":
                        matrix[0][j] = "C"

        # Iterate first row and zeroe marked columns
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == "C":
                self.clear_col(matrix, j)

        for i in range(1, len(matrix)):
            if matrix[i][0] == "R":
                self.clear_row(matrix, i)

        if matrix[0][0] == "B":
            self.clear_col(matrix, 0)
            self.clear_row(matrix, 0)
        elif matrix[0][0] == "C":
            self.clear_col(matrix, 0)
        elif matrix[0][0] == "R":
            self.clear_row(matrix, 0)

    def clear_row(self, matrix, row_index):
        for y in range(len(matrix[0])):
            matrix[row_index][y] = "0"

    def clear_col(self, matrix, col_index):
        for x in range(len(matrix)):
            matrix[x][col_index] = "0"
        

if __name__ == "__main__":
    s = Solution()
    # matrix = [[1,1,1],[1,0,1],[1,1,1]]
    # s.setZeroes(matrix)
    # print(matrix)
    # matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    # s.setZeroes(matrix)
    # print(matrix)
    # matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
    # s.setZeroes(matrix)
    # print(matrix)
    matrix = [[8,3,6,9,7,8,0,6],[0,3,7,0,0,4,3,8],[5,3,6,7,1,6,2,6],[8,7,2,5,0,6,4,0],[0,2,9,9,3,9,7,3]]
    s.setZeroes(matrix)
    print(matrix)