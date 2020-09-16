# sliding window
# start from zero and increase the window size (end) if no dups are found
# check if that substring is the longest
# if we find dup, then we reduce the window size by increasing the start
# we keep iterating until we traverse the whole string and


class Solution:
    def lengthOfLongestSubstring(self, s):
        if s == "" or s is None:
            return 0

        start = 0
        end = 1
        longest_substr = 1
        substr = s[0]
        ocurrences = {}
        ocurrences[s[0]] = 1
        length = len(s)

        while start < end and end < length:
            char = s[end]
            substr += char

            #print(f"processing char: {char} - substr: {substr}")
            if char in ocurrences:
                ocurrences[char] += 1
                while self.has_duplicate(ocurrences):
                    first_char = substr[0]
                    #print(f"duplicate found, shrinking window - first_char: {first_char} - substr: {substr} - ocurrences: {ocurrences} - start: {start} - end: {end}")
                    ocurrences[first_char] -= 1
                    if ocurrences[first_char] == 0:
                        del ocurrences[first_char]
                    
                    start += 1
                    substr = s[start:end + 1]
                    #print(f"after shrinking window - substr: {substr} - ocurrences: {ocurrences} - start: {start} - end: {end}")
            else:
                ocurrences[char] = 1
            
            end += 1
    
            if len(substr) > longest_substr:
                longest_substr = len(substr)
            #print(f"=== substr: {substr} - longest_substr: {longest_substr}")

        return longest_substr
            
    def has_duplicate(self, ocurrences):
        for o in ocurrences:
            if ocurrences[o] > 1:
                return True
        return False
            


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring(""))
    print(s.lengthOfLongestSubstring("askldjklasj & *(( 6y8u687 2369"))