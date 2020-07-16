def remove_duplicates(arr):
    non_dup_pointer = 0

    for index in range(1, len(arr)):
        if arr[index] != arr[non_dup_pointer]:
            non_dup_pointer += 1
            arr[non_dup_pointer] = arr[index]

    return non_dup_pointer + 1


if __name__ == "__main__":
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 2, 2, 11]))
    print(remove_duplicates([2, 2, 2, 11]))