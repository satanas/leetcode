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

# Second approach using a hashmap instead of sorting

class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        
        start = 0
        end = len(p) - 1
        p_dict = {}
        s_dict = {}
        for i in range(len(p)):
            self.update_hashmap(p_dict, "", p[i])
            self.update_hashmap(s_dict, "", s[i])
        length_p = len(p)
        substring = ""
        results = []
        while end <= len(s) - 1:
            if end - start > length_p - 1:
                start += 1
                self.update_hashmap(s_dict, s[start - 1], s[end])
            # print(f"start: {start} - end: {end}")
            # print(f"pdict: {p_dict} - sdict: {s_dict}")
            if p_dict == s_dict:
                results.append(start)
            end += 1
        return results

    def update_hashmap(self, hashmap, old_char, new_char):
        if new_char in hashmap:
            hashmap[new_char] += 1
        else:
            hashmap[new_char] = 1

        if old_char in hashmap:
            hashmap[old_char] -= 1
            if hashmap[old_char] <= 0:
                del hashmap[old_char]

if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))
    print(s.findAnagrams("abab", "ab"))
    print(s.findAnagrams("", "ab"))
    print(s.findAnagrams("ab", "abcd"))
    print(s.findAnagrams("      ", "ab"))