# Questions:
# 1. What happens if we get something like "4358oiuy"?

class Solution:
    INT_MAX = pow(2, 31) - 1
    INT_MIN = -pow(2, 31)

    def myAtoi(self, string):
        string = string.lstrip(" ")
        if len(string) == 0:
            return 0
        first_non_whitespace = string[0]

        if first_non_whitespace != "-" and first_non_whitespace != "+" and not self.is_number(first_non_whitespace):
            return 0
        
        if len(string) > 1 and (first_non_whitespace == "-" or first_non_whitespace == "+") and not self.is_number(string[1]):
            return 0

        negative_mult = 1
        if first_non_whitespace == "-":
            negative_mult = -1
            string = string[1:]
        elif first_non_whitespace == "+":
            string = string[1:]

        next_whitespace = 0
        for i, c in enumerate(string):
            if not self.is_number(c):
                next_whitespace = i
                break

        string = string[:next_whitespace] if next_whitespace > 0 else string
        total = len(string)
        if total == 0:
            return 0
        
        num = 0
        for i, x in enumerate(string):
            mult = total - (i + 1)
            val = ord(x) - 48
            num += val * pow(10, mult)
        num *= negative_mult
        if num >= self.INT_MAX:
            return self.INT_MAX
        elif num <= self.INT_MIN:
            return self.INT_MIN
        else:
            return num

    def is_number(self, char):
        return ord(char) >= 48 and ord(char) <= 57

    def find_first_non_whitespace(self, string):
        for i, c in enumerate(string):
            if not self.is_number(c) and c != "-" and first_non_whitespace != "+":
                continue
            else:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("42"))
    print(s.myAtoi("   -42"))
    print(s.myAtoi("4193 with words"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi("-91283472332"))
    print(s.myAtoi("3.14159"))
    print(s.myAtoi(""))
    print(s.myAtoi("+1"))
    print(s.myAtoi("+-2"))
    print(s.myAtoi("  -0012a42"))
    