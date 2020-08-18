# Input: a = 2, b = 3
# 8 4 2 1
# 0 0 1 0   a
# 0 0 1 1   b
# === a & b
# 0 0 1 0   carry
# === a ^ b
# 0 0 0 1  new a
# === carry << 1
# 0 1 0 0  new b
# === a & b
# 0 0 0 0  carry
# === a ^ b
# 0 1 0 1  new a
# === carry << 1
# 0 0 0 0  new b

class Solution:
    def getSum(self, a, b):
        if a >= 0 and b >= 0:
            return self.addition(a, b)
        elif a < 0 or b < 0:
            if a > b:
                return self.substraction(abs(a), abs(b))
            else:
                return self.substraction(abs(b), abs(a))
            #else:
                #return self.substraction(a, b)

    def addition(self, a, b):
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

    def substraction(self, a, b):
        while b != 0:
            borrow = (~a) & b
            a = a ^ b
            b = borrow << 1
        return a

        
if __name__ == "__main__":
    s = Solution()
    print(s.substraction(1, 5))
    print(s.getSum(-2, 3))
    print(s.getSum(1, 3))
    print(s.getSum(3, 2))
    print(s.getSum(-5, 1))