def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append("")
    max_len = len(str)

    for c in str:
        upper_c = c.upper()
        new_set = []
        for i in range(len(permutations)):
            new_item = permutations[i] + c
            
            new_set.append(new_item)

            if c != upper_c:
                new_item = permutations[i] + upper_c
                new_set.append(new_item)
        permutations = new_set

    return permutations

if __name__ == "__main__":
    print("String permutations are: " +
                str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
                str(find_letter_case_string_permutations("ab7c")))