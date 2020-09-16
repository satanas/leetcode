# Use one array per row
# Start iterating the string and putting each char in an index
# Increase this index until we reach numRows - 1
# Then, decrease the index until we reach 0
# Repeat the above process until we reach the end of the string

"PAYPALISHIRING"
i = -1
row = ["PA", "AP", "Y"]
delta = -1
char = "A"
numRows = 3

class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        if numRows == 0 or s == "" or s is None:
            return ""

        i = 0
        rows = []
        delta = 1

        for char in s:
            if len(rows) < numRows:
                rows.append(char)
            else:
                rows[i] += char
            i += delta

            if i == numRows:
                i = numRows - 2
                delta = -1
            elif i < 0:
                i = 1
                delta = 1

        return ''.join(rows)

if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))
    print(s.convert("PAYPALISHIRING", 4))
    print(s.convert("ABC", 1))
    print(s.convert("ABC", 0))
    print(s.convert("", 3))

        