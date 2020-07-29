def find_all_duplicates(nums):
    duplicateNumbers = []
    i = 0
    while i < len(nums):
        if nums[i] == i + 1:
            i += 1
        else:
            if nums[nums[i] - 1] == nums[i]:
                duplicateNumbers.append(nums[i])
                i += 1
            else:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
    return duplicateNumbers

if __name__ == "__main__":
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))