# 1. Function to convert integer to string
# 2. Function to reverse string
# 3. Function to convert string to int

MAX_INT = pow(2, 31) - 1
MIN_INT = -1 * pow(2, 31)

class Solution:
    def reverse(self, x):
        if x > MAX_INT or x < MIN_INT:
            return 0
        return self.str_to_int(self.reverse_string(self.int_to_str(x)))

    def int_to_str(self, i):
        return str(i)

    def str_to_int(self, s):
        x = int(s)
        if x > MAX_INT or x < MIN_INT:
            return 0
        return x

    def reverse_string(self, s):
        neg = False
        if s[0] == '-':
            neg = True
            s = s[1:]
        rs = ""
        for i in range(len(s) - 1, -1, -1):
            rs += s[i]
        return rs if not neg else "-" + rs

if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(120))
    print(s.reverse(0))
    print(s.reverse(8463847421))
    print(s.reverse(-9463847412))
    print(s.reverse(-0))
    print(s.reverse(1506000))