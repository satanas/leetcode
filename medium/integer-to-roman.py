# Take the number, substract something and repeat for the remainder
# 43 - 10 => X, 33
# 33 - 10 => XX, 23
# 23 - 10 => XXX, 13
# 13 - 10 => XXXX
# -- Check the last four and replace XXXX with XL
# 3 - 1 => XLI
# 2 - 1 => XLII
# 1 - 1 => XLIII

class Solution:
    def intToRoman(self, num):
        return self.recursive_conversion("", num)

    def recursive_conversion(self, curr_roman, num):
        # last_four = curr_roman[-4:]
        # last_digit = curr_roman[-1]
        # IIII => IV
        # IVIIII => IX
        
        # XXXX

        # if not is_valid(last_four):
        #     valid_roman = curr_roman[:-4]
        #     replacement = ""
        #     if last_digit == "M":
        #         replacement = "CM"
        #     elif last_digit == "X":
        #         replacement = "XL"
        #     elif last_digit == ""
        # print(f"Processing - roman: {curr_roman} - num: {num}")
        # input()
        if num == 1:
            return curr_roman + "I"
        elif num == 0:
            return curr_roman

        if num >= 1000:
            return self.recursive_conversion(curr_roman + "M", num - 1000)
        elif num < 1000 and num >= 500:
            if num >= 900:
                return self.recursive_conversion(curr_roman + "CM", num - 900)
            else:
                return self.recursive_conversion(curr_roman + "D", num - 500)
        elif num < 500 and num >= 100:
            if num >= 400:
                return self.recursive_conversion(curr_roman + "CD", num - 400)
            else:
                return self.recursive_conversion(curr_roman + "C", num - 100)
        elif num < 100 and num >= 50:
            if num >= 90:
                return self.recursive_conversion(curr_roman + "XC", num - 90)
            else:
                return self.recursive_conversion(curr_roman + "L", num - 50)
        elif num < 50 and num >= 10:
            if num >= 40:
                return self.recursive_conversion(curr_roman + "XL", num - 40)
            else:
                return self.recursive_conversion(curr_roman + "X", num - 10)
        elif num < 10 and num >= 5:
            if num >= 9:
                return self.recursive_conversion(curr_roman + "IX", num - 9)
            else:
                return self.recursive_conversion(curr_roman + "V", num - 5)
        elif num >= 4:
            return self.recursive_conversion(curr_roman + "IV", num - 4)
        elif num < 4 and num > 1:
            return self.recursive_conversion(curr_roman + "I", num - 1)
        elif num == 1:
            return curr_roman + "I"
        elif num == 0:
            return curr_roman

if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(43))
    print(s.intToRoman(99))

# LXXXXVIIII
# XCIX