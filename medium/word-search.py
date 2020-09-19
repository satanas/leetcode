# User recursion
# Iterate the matrix and check from each position
# Ignore those paths where the letter is not the same
# Keep track of the visited nodes
# Return false if there are no more node adjacents available or if we reached the length of the string and didn't find the word


class Solution:
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.recursive_search(i, j, [], board, word):
                    return True
        return False

    def recursive_search(self, x, y, visited, board, word):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            print(f"border x: {x} - y: {y}")
            return False

        if (x, y) in visited:
            print(f"visited x: {x} - y: {y}")
            return False

        print(f"checking x: {x} - y: {y} - letter: {board[x][y]} - visited: {visited}")

        if board[x][y] != word[0]:
            print(f"chao")
            return False

        if board[x][y] == word[0] and len(word) == 1:
            return True

        new_visited = visited[:]
        new_visited.append((x, y))
        # Check adjacents
        return self.recursive_search(x - 1, y, new_visited, board, word[1:]) or \
                self.recursive_search(x + 1, y, new_visited, board, word[1:]) or \
                self.recursive_search(x, y + 1, new_visited, board, word[1:]) or \
                self.recursive_search(x, y - 1, new_visited, board, word[1:])
        

if __name__ == "__main__":
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    board2 = []
    board3 = [[]]
    board4 = [
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]
    ]
    s = Solution()
    # print(s.exist(board, "ABCCED"))
    # print(s.exist(board, "SEE"))
    # print(s.exist(board, "ABCB"))
    # print(s.exist(board3, "ABC"))
    print(s.exist(board4, "ABCESEEEFS"))