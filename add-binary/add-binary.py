from functools import reduce

class Solution:
    def addBinary(self, a, b):
        int_a = self.bin_str_to_int(a)
        int_b = self.bin_str_to_int(b)
        return self.int_to_bin_str(int_a + int_b)

    def bin_str_to_int(self, bin_str):
        exps = [(len(bin_str) - idx - 1, c) for idx, c in enumerate(bin_str)]
        elements = list(map(lambda x: pow(2, x[0]) if x[1] == '1' else 0, exps))
        return reduce(lambda x, y: x + y, elements)

    def int_to_bin_str(self, value):
        bin_str = ""
        while True:
            bin_str += "1" if value % 2 == 1 else "0"
            value //= 2
            if value <= 0:
                break
        return bin_str[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("0", "0"))