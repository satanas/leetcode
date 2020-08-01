def find_subsets(nums):
    subsets = []
    last_num = None
    last_subset = []
    subsets.append(last_subset)
    nums.sort()

    for x in nums:
        curr_subset = new_set if x == last_num else subsets
        new_set = []

        for i in range(len(curr_subset)):
            new_item = list(curr_subset[i])
            new_item.append(x)
            new_set.append(new_item)
        subsets += new_set
        last_num = x

    return subsets


if __name__ == "__main__":
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))