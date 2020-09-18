# "2216"
# 2, 21, 6 => [B, U, F]
# 22, 1, 6 => [V, A, F]
# 22, 16 => [V, U]
# 2, 2, 1, 6 => [B, B, A, F]
# 2, 2, 16 => [B, B, U]

# Trying to generate all posible combinations
# While we generate the combinations, we can parse them (not necessary)
# Two options: single digit and digits combined

# We can solve this with subsets
# Iterate each character and combine them (using the rules) with the previous results
# Then return the total combinations generated


class Solution:

    VALID_WITH_ZERO = ["10", "20"]

    def numDecodings(self, s):
        if s[0] == "0":
            return 0

        results = [[s[0]]]
        for num in s[1:]:
            new_results = []
            for item in results:
                last_digit = item[-1]
                print(f"processing item: {item} - last_digit: {last_digit} - num: {num}")
                first_item = list(item)
                if num != "0":
                    first_item.append(num)
                print(f"adding first item: {first_item}")
                new_results.append(first_item)
                if len(last_digit) <= 1:
                    temp = last_digit + num
                    print(f"temp: {temp}")
                    if int(temp) <= 26:
                        new_item = item[:-1]
                        new_item.append(temp)
                        print(f"adding new item: {new_item}")
                        new_results.append(new_item)
                print(new_results)
            results = new_results
        return len(results)

if __name__ == "__main__":
    s = Solution()
    # print(s.numDecodings("12"))
    # print(s.numDecodings("226"))
    # print(s.numDecodings("2216"))
    # print(s.numDecodings("0"))
    # print(s.numDecodings("7"))
    # print(s.numDecodings("10"))
    # print(s.numDecodings("00"))
    # print(s.numDecodings("0010110"))
    print(s.numDecodings("206"))

        