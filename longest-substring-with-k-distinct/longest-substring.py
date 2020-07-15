def longest_substring_with_k_distinct(str, k):
    window_start = 0
    longest_substr = 0
    window_string = []

    for window_end, char in enumerate(str):
        window_string.append(char)
        unique_chars = gi
        
        if unique_chars <= k:
            longest_substr = max(longest_substr, len(window_string))
        else:
            while unique_chars > k:
                window_string = window_string[1:]
                unique_chars = len(set(window_string))
                if len(window_string) == 1:
                    break
    return longest_substr

if __name__ == "__main__":
    print(longest_substring_with_k_distinct("araaci", 2))
    print(longest_substring_with_k_distinct("araaci", 1))
    print(longest_substring_with_k_distinct("cbbebi", 3))