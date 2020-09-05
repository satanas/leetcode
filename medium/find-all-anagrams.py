# Input:
# s: "cbaebabacd" p: "abc"
# p's anagrams are: "abc", "acb", "bca", "bac", "cba", "cab"

# To detect an anagram, we can sort the sub-string an compare it with the sorted version of p
# Use a sliding window of k to iterate the string (k = len(p))

# While our slide window is still valid
# Build a substring with the elements of the sliding window (taking care of adding/removing chars accordingly)
# Sort the substring and compare it with the sorted version of p
# If they are equal, we push the index of the start of the sliding window to the results array
# We slide the window one more char

class Solution:
    def findAnagrams(self, s, p):
        start = 0
        end = 0
        sorted_p = self.sort_string(p)
        lenght_p = len(p)
        substring = ""
        results = []
        while end <= len(s):
            if end - start > lenght_p:
                substring = substring[1:]
                start += 1
            if end - start == lenght_p:
                sorted_substring = self.sort_string(s[start:end])
                if sorted_substring == sorted_p:
                    results.append(start)
            end += 1
        return results

    def sort_string(self, str):
        return ''.join(sorted(str))


if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))
    print(s.findAnagrams("abab", "ab"))
    print(s.findAnagrams("", "ab"))
    print(s.findAnagrams("ab", "abcd"))