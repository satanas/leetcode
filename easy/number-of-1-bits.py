# 8 4 2 1 = 13
# 1 1 0 1 

# 2^?
# 2 ^ 3 = 8
# 13 // 8 = 1 (int div)
# remain = 13 % 8 = 5
# ===
# 2 ^ 2 = 4
# 5 // 4 = 1
# remain = 5 % 4 = 1
# ===
# 2 ^ 1 = 2
# 1 // 2 = 0
# remain = 1 % 2 = 1
# ===
# 2 ^ 0 = 1
# 1 // 1 = 1
# remain = 1 % 1 = 0

# Algorithm
# 1. Identify the max exponent of 2 for the given number (x)
# 2. Starting from x, we perform the int division of num (given number) by 2 ^ x
# if result > 0 then:
#   we increment a counter
# Set the new num as the mod the num % 2 ^ x
# repeat until num == 0

# Algorithm 2:
# Use two pointers to iterate the string and count the numbers
# start = 0, end = len(n)
# on each step we move the pointers towards the center until they meet
#      2/2
# 1  0  1  0  1
# c = 2

class Solution2:
    def hammingWeight(self, n):
        weight = 0
        start = 0
        end = len(n) - 1

        while start < end:
            print(f"n[{start}] = {n[start]} - n[{end}] = {n[end]} - weight: {weight}")
            weight += 1 if n[start] == "1" else 0
            start += 1
            weight += 1 if n[end] == "1" and start < end else 0
            end -= 1
        return weight

class Solution:
    def hammingWeight(self, n):
        mask = 0x1
        weight = 0
        while n > 0:
            if n & mask == 1:
                weight += 1
            n = n >> 1
        return weight




if __name__ == "__main__":
    s = Solution()
    print(s.hammingWeight("00000000000000000000000000001011"))
    print(s.hammingWeight("00000000000000000000000010000000"))
    print(s.hammingWeight("11111111111111111111111111111101"))