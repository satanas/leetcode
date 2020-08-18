class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for m in range(len(matrix)): # iterate all rows first
            print(f'm: {m} - matrix[{m}]: {matrix[m]}')
            for n in range(len(matrix[0])):
                if matrix[m][n] == 0:
                    # mark the last row at the n column
                    matrix[len(matrix) - 1][n] = pow(10, 9) + 2
                    # mark the current row at the last column
                    matrix[m][len(matrix[n]) - 1] = pow(10, 9) + 1

        for m in range(len(matrix)):
            print(f'm: {m} - matrix[{m}]: {matrix[m]}')
            for n in range(len(matrix[0])):
                print(f'n: {n}')
                if matrix[m][len(matrix[n]) - 1] == pow(10, 9) + 1:
                    matrix[m][n] = 0
                if matrix[len(matrix) - 1][n] == pow(10, 9) + 2:
                    matrix[m][n] = 0
        return matrix

if __name__ == "__main__":
    s = Solution()
    print(s.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
    print(s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))