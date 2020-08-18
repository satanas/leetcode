class Solution:
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s

        longest = ""
        for start in range(len(s)):
            for end in range(len(s), start, -1):
                string1 = ""
                string2 = ""
                for i in range(end - start):
                    string1 += s[start + i]
                    string2 += s[end - 1 - i]

                if string1 == string2 and len(string1) > len(longest):
                    longest = string1
        return longest
                

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("a"))
    print(s.longestPalindrome("bb"))
    print(s.longestPalindrome("ashuuuuhaaahdhaha"))