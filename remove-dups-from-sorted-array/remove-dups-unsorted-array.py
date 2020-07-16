def remove_duplicates(arr, k):
    non_dup_index = 0

    for index in range(len(arr)):
        if arr[index] != k:
            arr[non_dup_index] = arr[index]
            non_dup_index += 1
    
    return non_dup_index



if __name__ == "__main__":
    print(remove_duplicates([3, 2, 3, 6, 3, 10, 9, 3], 3))
    print(remove_duplicates([2, 11, 2, 2, 1], 2))
    print(remove_duplicates([2, 2, 2, 11], 2))
    print(remove_duplicates([2, 2, 2, 2], 2))