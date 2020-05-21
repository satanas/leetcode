class Solution:
    def plusOne(self, digits):
        integer = self.to_integer(digits)
        return self.to_array(integer + 1)

    def to_integer(self, digits):
        value = 0
        for i, x in enumerate(digits):
            mult = pow(10, (len(digits) - 1 - i))
            value += x * mult
        return value

    def to_array(self, integer):
        return [c for c in str(integer)]

if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([4, 3, 2, 1]))